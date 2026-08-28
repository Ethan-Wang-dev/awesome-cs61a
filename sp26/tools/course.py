#!/usr/bin/env python3
"""Small local workflow for the Spring 2026 CS61A assignments."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = Path(__file__).with_name("assignments.json")
REQUIRED_FIELDS = {
    "id",
    "kind",
    "path",
    "editable",
    "runner",
    "source_archive",
    "instructions",
    "runnable",
    "optional",
}


def _relative_path(value: Any, *, assignment_id: str, field: str) -> Path:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{assignment_id}: {field} must be a non-empty string")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"{assignment_id}: {field} must stay inside the repository")
    return path


def _validate_entry(item: Any) -> dict[str, Any]:
    if not isinstance(item, dict):
        raise ValueError("Each assignment entry must be an object")

    missing = REQUIRED_FIELDS - item.keys()
    if missing:
        missing_fields = ", ".join(sorted(missing))
        raise ValueError(f"Assignment entry is missing: {missing_fields}")

    assignment_id = item["id"]
    if not isinstance(assignment_id, str) or not assignment_id:
        raise ValueError("Assignment id must be a non-empty string")
    _relative_path(item["path"], assignment_id=assignment_id, field="path")

    editable = item["editable"]
    if not isinstance(editable, list) or not all(
        isinstance(path, str) and path and not Path(path).is_absolute()
        and ".." not in Path(path).parts
        for path in editable
    ):
        raise ValueError(f"{assignment_id}: editable must contain repository-relative paths")

    if not isinstance(item["kind"], str) or not item["kind"]:
        raise ValueError(f"{assignment_id}: kind must be a non-empty string")
    if not isinstance(item["runnable"], bool) or not isinstance(item["optional"], bool):
        raise ValueError(f"{assignment_id}: runnable and optional must be booleans")
    if item["runnable"] and item["runner"] != "ok":
        raise ValueError(f"{assignment_id}: runnable entries must use the ok runner")
    if not item["runnable"] and item["runner"] is not None:
        raise ValueError(f"{assignment_id}: documentation entries cannot define a runner")
    if not isinstance(item["instructions"], str) or not item["instructions"]:
        raise ValueError(f"{assignment_id}: instructions must be a URL")

    return item


def load_manifest() -> list[dict[str, Any]]:
    """Load and structurally validate the assignment manifest."""
    try:
        payload = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Manifest not found: {MANIFEST_PATH}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Manifest is not valid JSON: {exc}") from exc

    assignments = payload.get("assignments") if isinstance(payload, dict) else None
    if not isinstance(assignments, list):
        raise ValueError("Manifest must contain an assignments list")
    return [_validate_entry(item) for item in assignments]


def assignment_index(assignments: Iterable[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Return assignments by id and reject duplicate identifiers."""
    index: dict[str, dict[str, Any]] = {}
    for item in assignments:
        assignment_id = item["id"]
        if assignment_id in index:
            raise ValueError(f"Duplicate assignment id: {assignment_id}")
        index[assignment_id] = item
    return index


def _assignment_directory(item: dict[str, Any]) -> Path:
    return REPO_ROOT / _relative_path(
        item["path"], assignment_id=item["id"], field="path"
    )


def _edit_targets(item: dict[str, Any]) -> list[Path]:
    directory = _assignment_directory(item)
    return [directory / path for path in item["editable"]]


def _print_assignment(item: dict[str, Any]) -> None:
    markers = []
    if item["optional"]:
        markers.append("optional")
    if not item["runnable"]:
        markers.append("reading")
    marker = f" [{', '.join(markers)}]" if markers else ""
    targets = ", ".join(str(path.relative_to(REPO_ROOT)) for path in _edit_targets(item))
    edit_text = targets if targets else "open the assignment page"
    print(f"{item['id']:<16} {item['kind']:<9} {edit_text}{marker}")


def list_assignments(assignments: list[dict[str, Any]]) -> int:
    for item in assignments:
        _print_assignment(item)
    return 0


def _check_python() -> tuple[bool, str]:
    version = sys.version_info[:2]
    if version < (3, 10):
        return False, f"Python 3.10+ required (found {version[0]}.{version[1]})"
    return True, f"Python {version[0]}.{version[1]}"


def _check_ok(item: dict[str, Any]) -> tuple[bool, str]:
    directory = _assignment_directory(item)
    ok_path = directory / "ok"
    if not ok_path.is_file():
        return False, f"{item['id']}: missing ok runner"
    try:
        result = subprocess.run(
            [sys.executable, "ok", "--help"],
            cwd=directory,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=15,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, f"{item['id']}: could not start ok ({exc})"
    if result.returncode != 0:
        return False, f"{item['id']}: ok --help exited {result.returncode}"
    return True, f"{item['id']}: ok runner"


def doctor(assignments: list[dict[str, Any]]) -> int:
    checks: list[tuple[bool, str]] = [_check_python()]
    for item in assignments:
        directory = _assignment_directory(item)
        if directory.is_dir():
            checks.append((True, f"{item['id']}: directory"))
        else:
            checks.append((False, f"{item['id']}: missing directory {directory}"))
        for target in _edit_targets(item):
            if target.is_file():
                checks.append((True, f"{item['id']}: {target.name}"))
            else:
                checks.append((False, f"{item['id']}: missing edit target {target}"))
        if item["runnable"]:
            checks.append(_check_ok(item))

    for passed, message in checks:
        print(f"{'[OK]' if passed else '[FAIL]'} {message}")
    if all(passed for passed, _ in checks):
        print(f"All checks passed ({len(checks)} checks).")
        return 0
    failed = sum(not passed for passed, _ in checks)
    print(f"{failed} check(s) failed.", file=sys.stderr)
    return 1


def run_assignment(item: dict[str, Any], ok_args: list[str]) -> int:
    """Run one assignment's bundled ok.py in local mode."""
    directory = _assignment_directory(item)
    command = [sys.executable, "ok", "--local", "--nointeract", "--score", *ok_args]
    try:
        completed = subprocess.run(
            command,
            cwd=directory,
            input="n\n",
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as exc:
        print(f"Could not run {item['id']}: {exc}", file=sys.stderr)
        return 1

    print(f"\n== {item['id']} ==")
    output = completed.stdout + completed.stderr
    print(output, end="" if output.endswith("\n") else "\n")
    if completed.returncode != 0:
        return completed.returncode
    if re.search(r"# Error:|\bFailed:\s*[1-9]\d*\b", output):
        return 1
    return 0


def test_assignments(
    assignments: list[dict[str, Any]], assignment_id: str, ok_args: list[str]
) -> int:
    index = assignment_index(assignments)
    if assignment_id == "all":
        runnable = [item for item in assignments if item["runnable"]]
        results = [(item["id"], run_assignment(item, ok_args)) for item in runnable]
        print("\n== summary ==")
        for item_id, result in results:
            print(f"{'PASS' if result == 0 else 'FAIL':<5} {item_id} ({result})")
        return 0 if all(result == 0 for _, result in results) else 1

    item = index.get(assignment_id)
    if item is None:
        print(f"Unknown assignment: {assignment_id}", file=sys.stderr)
        return 2
    if not item["runnable"]:
        print(f"{assignment_id} is documentation-only and has no local test.", file=sys.stderr)
        return 2
    return run_assignment(item, ok_args)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("list", "doctor", "test"))
    parser.add_argument("assignment", nargs="?")
    parser.add_argument("ok_args", nargs=argparse.REMAINDER)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    try:
        assignments = load_manifest()
        assignment_index(assignments)
        if args.command == "list":
            if args.assignment or args.ok_args:
                parser.error("list does not accept extra arguments")
            return list_assignments(assignments)
        if args.command == "doctor":
            if args.assignment or args.ok_args:
                parser.error("doctor does not accept extra arguments")
            return doctor(assignments)
        if args.assignment is None:
            parser.error("test requires an assignment id or all")
        ok_args = list(args.ok_args)
        if ok_args and ok_args[0] == "--":
            ok_args.pop(0)
        return test_assignments(assignments, args.assignment, ok_args)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
