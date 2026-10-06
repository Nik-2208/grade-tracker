"""Regression tests for add-command validation and persistence."""

import contextlib
import csv
import io
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from grade_tracker.cli import main


class TestAddValidation(unittest.TestCase):
    """Exercise the public CLI before any grade row reaches the data file."""

    def run_add(self, data_path, *args):
        argv = ["grade_tracker", "--data", str(data_path), "add", *args]
        stdout = io.StringIO()
        stderr = io.StringIO()
        with mock.patch("sys.argv", argv), \
                contextlib.redirect_stdout(stdout), \
                contextlib.redirect_stderr(stderr):
            try:
                main()
            except SystemExit as exc:
                return exc.code, stdout.getvalue(), stderr.getvalue()
        return 0, stdout.getvalue(), stderr.getvalue()

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.data_path = Path(self.temp_dir.name) / "grades.csv"

    def read_rows(self):
        if not self.data_path.exists():
            return []
        with self.data_path.open(newline="", encoding="utf-8") as handle:
            return list(csv.DictReader(handle))

    def assert_rejected(self, *args, expected_error):
        code, stdout, stderr = self.run_add(self.data_path, *args)
        self.assertEqual(code, 2)
        self.assertIn(expected_error, stderr)
        self.assertNotIn("Added grade", stdout)
        self.assertEqual(self.read_rows(), [])

    def test_rejects_zero_max_score_without_writing(self):
        self.assert_rejected(
            "S1", "Mathematics", "50", "0", "not-a-date", "3", "1",
            expected_error="max_score must be greater than 0",
        )

    def test_rejects_score_above_max_without_writing(self):
        self.assert_rejected(
            "S1", "Mathematics", "101", "100", "2026-10-05", "3", "1",
            expected_error="score must be between 0 and max_score",
        )

    def test_rejects_negative_score_without_writing(self):
        self.assert_rejected(
            "S1", "Mathematics", "-1", "100", "2026-10-05", "3", "1",
            expected_error="score must be between 0 and max_score",
        )

    def test_rejects_malformed_date_without_writing(self):
        self.assert_rejected(
            "S1", "Mathematics", "50", "100", "not-a-date", "3", "1",
            expected_error="date must use YYYY-MM-DD format",
        )

    def test_rejects_impossible_calendar_date_without_writing(self):
        self.assert_rejected(
            "S1", "Mathematics", "50", "100", "2026-02-30", "3", "1",
            expected_error="date must be a valid calendar date",
        )

    def test_accepts_zero_score_boundary(self):
        code, stdout, stderr = self.run_add(
            self.data_path, "S1", "Mathematics", "0", "100", "2026-10-05", "3", "1"
        )
        self.assertEqual((code, stderr), (0, ""))
        self.assertIn("Added grade for S1", stdout)
        self.assertEqual(
            self.read_rows(),
            [{
                "student_id": "S1",
                "subject": "Mathematics",
                "score": "0.0",
                "max_score": "100.0",
                "date": "2026-10-05",
                "credits": "3.0",
                "semester": "1",
            }],
        )

    def test_accepts_score_equal_to_max_boundary(self):
        code, stdout, stderr = self.run_add(
            self.data_path, "S1", "Mathematics", "100", "100", "2026-10-05", "3", "1"
        )
        self.assertEqual((code, stderr), (0, ""))
        self.assertIn("Added grade for S1", stdout)
        self.assertEqual(len(self.read_rows()), 1)

    def test_accepts_normal_valid_input(self):
        code, stdout, stderr = self.run_add(
            self.data_path, "S1", "Mathematics", "50", "100", "2026-10-05", "3", "1"
        )
        self.assertEqual((code, stderr), (0, ""))
        self.assertIn("Added grade for S1", stdout)
        rows = self.read_rows()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["score"], "50.0")


if __name__ == "__main__":
    unittest.main()
