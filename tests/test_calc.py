"""Unit tests for calculation logic in grade_tracker."""

import unittest
from grade_tracker.calc import letter_grade, cgpa, sgpa, subject_average


class TestGradeCalculations(unittest.TestCase):

    def test_letter_grade_top_tier(self):
        """A score of 95/100 should return an 'A'."""
        self.assertEqual(letter_grade(95, 100), "A")

    def test_letter_grade_invalid_max_score(self):
        """A max_score <= 0 should raise ValueError."""
        with self.assertRaises(ValueError):
            letter_grade(50, 0)

    def test_cgpa_empty_returns_none(self):
        """Calculating CGPA on an empty list of grades should return None."""
        self.assertIsNone(cgpa([]))

    def test_sgpa_single_course(self):
        """Single course with score 95/100 should evaluate to 10.0 SGPA (A grade, 10.0 pts)."""
        grades = [{"student_id": "S1", "score": 95, "max_score": 100, "credits": 3, "semester": 1}]
        self.assertEqual(sgpa(grades, "S1", 1), 10.0)

    def test_cgpa_worked_example(self):
        """Worked example for CGPA and SGPA with credits."""
        grades = [
            {"student_id": "S1", "score": 95, "max_score": 100, "credits": 4, "semester": 1}, # A -> 10 * 4 = 40
            {"student_id": "S1", "score": 85, "max_score": 100, "credits": 3, "semester": 1}, # B -> 9 * 3 = 27
            {"student_id": "S1", "score": 75, "max_score": 100, "credits": 2, "semester": 2}, # C -> 8 * 2 = 16
        ]
        # SGPA Sem 1: (40 + 27) / 7 = 67 / 7 = 9.57
        self.assertEqual(sgpa(grades, "S1", 1), 9.57)
        # SGPA Sem 2: 16 / 2 = 8.0
        self.assertEqual(sgpa(grades, "S1", 2), 8.0)
        # CGPA: (40 + 27 + 16) / 9 = 83 / 9 = 9.22
        self.assertEqual(cgpa(grades, "S1"), 9.22)

    def test_subject_average_single_entry(self):
        """A single grade entry for a subject should return that score as average."""
        grades = [{"subject": "Mathematics", "score": 85, "max_score": 100}]
        self.assertEqual(subject_average(grades, "Mathematics"), 85.0)

    def test_subject_average_nonexistent(self):
        """Subject average should return None if no entries exist for that subject."""
        self.assertIsNone(subject_average([], "Physics"))

    def test_subject_average_mixed_max_scores(self):
        """Grades with different maximum scores should be averaged as percentages.

        Regression test for Issue #5: 35/50 and 70/100 are both 70%, so the
        average must be 70.0, not the raw-score average of 52.5.
        """
        grades = [
            {"subject": "Physics", "score": 35, "max_score": 50},
            {"subject": "Physics", "score": 70, "max_score": 100},
        ]
        self.assertEqual(subject_average(grades, "Physics"), 70.0)

    def test_subject_average_same_max_score(self):
        """When every grade shares a maximum score the average percentage matches the raw average."""
        grades = [
            {"subject": "Mathematics", "score": 80, "max_score": 100},
            {"subject": "Mathematics", "score": 90, "max_score": 100},
        ]
        self.assertEqual(subject_average(grades, "Mathematics"), 85.0)

    def test_subject_average_different_percentages(self):
        """Percentages that differ should be averaged, not raw scores."""
        grades = [
            {"subject": "Chemistry", "score": 45, "max_score": 50},   # 90%
            {"subject": "Chemistry", "score": 40, "max_score": 100},  # 40%
        ]
        self.assertEqual(subject_average(grades, "Chemistry"), 65.0)

    def test_letter_grade_boundaries(self):
        """checking letter grade boundaries"""
        self.assertEqual(letter_grade(90, 100), "A")
        self.assertEqual(letter_grade(80, 100), "B")
        self.assertEqual(letter_grade(70, 100), "C")
        self.assertEqual(letter_grade(60, 100), "D")
        self.assertEqual(letter_grade(59, 100), "F")


if __name__ == "__main__":
    unittest.main()
