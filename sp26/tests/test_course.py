import contextlib
import io
import subprocess
import sys
import unittest

from sp26.tools import course


class CourseWorkflowTests(unittest.TestCase):
    def capture_main(self, argv):
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
            result = course.main(argv)
        return result, stream.getvalue()

    def test_manifest_has_unique_ids_and_edit_targets(self):
        assignments = course.load_manifest()
        ids = [item["id"] for item in assignments]

        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(assignments), 16)
        for item in assignments:
            self.assertIn("path", item)
            self.assertIn("editable", item)

    def test_every_editable_path_exists(self):
        for item in course.load_manifest():
            for relative_path in item["editable"]:
                self.assertTrue(
                    (course.REPO_ROOT / item["path"] / relative_path).is_file(),
                    f"missing edit target for {item['id']}: {relative_path}",
                )

    def test_list_prints_edit_target(self):
        result, output = self.capture_main(["list"])

        self.assertEqual(result, 0)
        self.assertIn("hw01", output)
        self.assertIn("hw01.py", output)
        self.assertIn("scheme-contest", output)

    def test_list_marks_reading_and_optional_entries(self):
        result, output = self.capture_main(["list"])

        self.assertEqual(result, 0)
        self.assertIn("hw11", output)
        self.assertIn("reading", output)
        self.assertIn("optional", output)

    def test_doctor_passes_for_checked_out_starters(self):
        result, output = self.capture_main(["doctor"])

        self.assertEqual(result, 0, output)
        self.assertIn("All checks passed", output)

    def test_unknown_assignment_returns_an_error(self):
        result, output = self.capture_main(["test", "unknown"])

        self.assertNotEqual(result, 0)
        self.assertIn("Unknown assignment", output)

    def test_documentation_entry_cannot_be_run(self):
        result, output = self.capture_main(["test", "hw11"])

        self.assertNotEqual(result, 0)
        self.assertIn("documentation-only", output)

    def test_incomplete_starter_does_not_leave_runner_input_error(self):
        completed = subprocess.run(
            [
                sys.executable,
                str(course.REPO_ROOT / "sp26/tools/course.py"),
                "test",
                "hw01",
                "--",
                "--question",
                "a_plus_abs_b",
            ],
            input="n\n",
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertNotEqual(completed.returncode, 0)
        self.assertNotIn("EOFError", completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
