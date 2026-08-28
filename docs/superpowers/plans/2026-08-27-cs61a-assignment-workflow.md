# CS61A Assignment Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a ready-to-edit Spring 2026 CS61A workspace with all homework/project starters, one assignment map, and a local test workflow that keeps study friction low.

**Architecture:** Official starter packages are expanded into `sp26/homework/` and `sp26/projects/`, while a single JSON manifest records paths, edit targets, source URLs, and runner behavior. A standard-library Python CLI reads that manifest to list assignments, validate setup, and invoke each package's bundled `ok` runner with network disabled. Workflow tests exercise the manifest and CLI without running assignment graders.

**Tech Stack:** Python 3.10+, Python standard library (`argparse`, `json`, `subprocess`, `unittest`), Berkeley `ok` runner bundled with each starter package, Markdown documentation.

**Spec:** `docs/superpowers/specs/2026-08-27-cs61a-assignment-workflow.md`

## Global Constraints

- Cover HW01–HW10, a documentation-only HW11 entry, Hog/Cats/Ants/Scheme, and optional Scheme Contest.
- Keep videos, slides, discussion PDFs, lab PDFs, and answer files external; import only programming starter/test/runtime files.
- Preserve the official package layout required by tests and runtime assets.
- Use Python 3.10+ and only the standard library for the workflow tool and its tests.
- `ok` invocations must use local mode and propagate the assignment result; workflow checks must not require network access.
- All new documentation, scripts, and metadata use English.

---

### Task 1: Import starters and create the assignment manifest

**Files:**
- Create: `sp26/homework/hw01/` through `sp26/homework/hw10/` from the corresponding Spring 2026 starter archives.
- Create: `sp26/projects/hog/`, `cats/`, `ants/`, `scheme/`, and `optional/scheme-contest/` from the corresponding archives.
- Create: `sp26/homework/hw11/README.md`
- Create: `sp26/tools/assignments.json`

**Interfaces:**
- Produces the paths and records consumed by `course.py` and `ASSIGNMENTS.md`.
- Each runnable record has `id`, `kind`, `path`, `editable`, `runner`, `source_archive`, `instructions`, and `runnable` fields.

- [ ] **Step 1: Verify source archives and extract them into the documented paths**

Use the pinned source repository `https://github.com/LR2933/cs61a-spring-2026` and its `hw/<id>/<id>.zip` or `proj/<name>/<name>.zip` archives. Strip the archive's one top-level directory while extracting so `hw01.py` lands at `sp26/homework/hw01/hw01.py`; preserve tests, `ok`, `.ok`, interpreters, and required project assets. Do not extract any `sol-*` archive.

- [ ] **Step 2: Record exact edit targets in `assignments.json`**

Use this schema for every entry:

```json
{
  "id": "hw01",
  "kind": "homework",
  "path": "sp26/homework/hw01",
  "editable": ["hw01.py"],
  "runner": "ok",
  "source_archive": "https://raw.githubusercontent.com/LR2933/cs61a-spring-2026/main/hw/hw01/hw01.zip",
  "instructions": "https://cs61a.org/hw/hw01/",
  "runnable": true,
  "optional": false
}
```

Use `hw07.scm`, `hw08.scm`, `hw09.scm`, and `hw10.sql` for the Scheme/SQL homework edit targets. Set HW11 `runnable` to `false` with an empty `editable` list. Set Scheme Contest `optional` to `true`.

- [ ] **Step 3: Add the HW11 documentation entry**

Write a short English README linking to the Spring 2026 HW11 page, explaining that the finale consists of surveys/reflection and has no code submission.

- [ ] **Step 4: Commit the imported baseline**

```bash
git add sp26/homework sp26/projects sp26/tools/assignments.json
git commit -m "feat(sp26): add homework and project starters"
```

### Task 2: Write failing tests for the workflow CLI

**Files:**
- Create: `sp26/tests/test_course.py`
- Test target: `sp26/tools/course.py` (intentionally absent at the start of this task)

**Interfaces:**
- Tests import `course.load_manifest`, `course.assignment_index`, and invoke `course.main(argv)`.
- Later implementation must return integer exit codes and avoid network calls for `doctor` and `list`.

- [ ] **Step 1: Write the manifest and list tests**

```python
def test_manifest_has_unique_ids_and_edit_targets():
    assignments = course.load_manifest()
    ids = [item["id"] for item in assignments]
    self.assertEqual(len(ids), len(set(ids)))
    for item in assignments:
        self.assertIn("path", item)
        self.assertIn("editable", item)

def test_list_prints_edit_target(capsys):
    self.assertEqual(course.main(["list"]), 0)
    self.assertIn("hw01", capsys.readouterr().out)
    self.assertIn("hw01.py", capsys.readouterr().out)
```

Use `contextlib.redirect_stdout` in the actual unittest implementation so the suite has no pytest dependency.

- [ ] **Step 2: Add path and command-validation tests**

Cover `doctor` returning zero on the checked-out starter tree, an unknown id returning a non-zero code with an error, and HW11 returning a non-zero code with a documentation-only message. Assert every editable path exists.

- [ ] **Step 3: Run the tests and verify the expected RED state**

Run:

```bash
python3 -m unittest sp26.tests.test_course -v
```

Expected: collection fails because `sp26/tools/course.py` has not been implemented yet. Fix test import paths only if the failure comes from the test harness rather than the missing CLI.

- [ ] **Step 4: Commit the failing tests**

```bash
git add sp26/tests/test_course.py
git commit -m "test(sp26): define assignment workflow behavior"
```

### Task 3: Implement the standard-library CLI

**Files:**
- Create: `sp26/tools/course.py`
- Modify: `sp26/tests/test_course.py` only when a test assertion needs correction after the RED verification.

**Interfaces:**
- `load_manifest() -> list[dict]` loads `assignments.json` relative to `course.py`.
- `assignment_index(assignments: list[dict]) -> dict[str, dict]` rejects duplicate ids.
- `main(argv: list[str] | None = None) -> int` implements `list`, `doctor`, and `test`.
- `run_assignment(item: dict, ok_args: list[str]) -> int` executes `python3 ok --local --nointeract` in the assignment directory and returns its exit code.

- [ ] **Step 1: Implement manifest loading and validation**

Resolve the repository root with `Path(__file__).resolve().parents[2]`. Validate required keys, relative paths, unique ids, and that every `editable` path exists. Raise a user-facing `ValueError` with the assignment id and missing field.

- [ ] **Step 2: Implement `list` and `doctor`**

`list` prints one compact line per entry: id, kind, edit target(s), and an `optional`/`reading` marker. `doctor` checks Python major/minor `>= 3.10`, all assignment directories, edit targets, and `python3 ok --help` for runnable entries. It prints a summary and returns 0 only when all checks pass.

- [ ] **Step 3: Implement local test dispatch**

For `test <id>`, reject unknown and documentation-only ids, run the package's `ok` executable with `--local --nointeract`, and pass any arguments after `--` through unchanged. For `test all`, run every runnable item in manifest order, continue after failures, print a pass/fail summary, and return 0 only when all entries pass.

- [ ] **Step 4: Run the focused tests and verify GREEN**

Run:

```bash
python3 -m unittest sp26.tests.test_course -v
python3 sp26/tools/course.py list
python3 sp26/tools/course.py doctor
```

Expected: all workflow tests pass; `list` shows edit targets; `doctor` reports every starter and `ok` runner as healthy. Running an unfinished assignment may fail its own grader, which is expected.

- [ ] **Step 5: Commit the CLI**

```bash
git add sp26/tools/course.py sp26/tests/test_course.py
git commit -m "feat(sp26): add local assignment workflow CLI"
```

### Task 4: Add learner-facing documentation

**Files:**
- Create: `sp26/ASSIGNMENTS.md`
- Create: `sp26/homework/README.md`
- Create: `sp26/projects/README.md`
- Modify: `README.md`
- Modify: `README.zh-CN.md`
- Modify: `sp26/README.md`

**Interfaces:**
- Documentation links every manifest id to its relative directory, editable file, official instructions, and exact local test command.
- The root README remains bilingual; new child documentation is English.

- [ ] **Step 1: Write the assignment index from the manifest**

Create tables for homework and projects. Keep the first action visible: open the listed file, implement one question at a time, then run `python3 sp26/tools/course.py test <id>`.

- [ ] **Step 2: Add concise homework/project workflow guides**

Explain the edit/test loop, how to run a single `ok` question through the CLI passthrough, and where official instructions live. Mention HW11 and Scheme Contest status.

- [ ] **Step 3: Link the new workflow from existing READMEs**

Add the assignment index to the root and SP26 “start here” sections without changing the repository's existing course-route content.

- [ ] **Step 4: Commit documentation**

```bash
git add README.md README.zh-CN.md sp26/README.md sp26/ASSIGNMENTS.md sp26/homework/README.md sp26/projects/README.md
git commit -m "docs(sp26): document assignment edit and test loop"
```

### Task 5: Verify the complete learner workflow

**Files:**
- Test: `sp26/tests/test_course.py`
- Verify: all files under `sp26/homework/` and `sp26/projects/`

- [ ] **Step 1: Run workflow unit tests**

```bash
python3 -m unittest discover -s sp26/tests -v
```

Expected: all tests pass.

- [ ] **Step 2: Run setup diagnostics**

```bash
python3 sp26/tools/course.py doctor
```

Expected: Python, manifest, editable files, package directories, and every `ok --help` check pass.

- [ ] **Step 3: Exercise representative assignment runners**

```bash
python3 sp26/tools/course.py test hw01 -- --question a_plus_abs_b
python3 sp26/tools/course.py test hog -- --question 0
```

Expected: commands reach the bundled grader and return its status without network authentication. Starter code can fail tests until the learner implements it.

- [ ] **Step 4: Inspect repository hygiene**

```bash
git status --short
git ls-files | rg '(^|/)(sol-|\.env|__pycache__|ok_backup|\.DS_Store)'
```

Expected: no solution archives, credentials, generated caches, or editor state are tracked.

- [ ] **Step 5: Commit verification metadata if needed and report the final state**

Use a focused commit only for required `.gitignore` or documentation adjustments. Report the final verification commands and the first file the learner should open (`sp26/ASSIGNMENTS.md`).
