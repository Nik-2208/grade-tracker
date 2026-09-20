"""Unit tests for calculation logic in grade_tracker."""

import unittest
from grade_tracker.calc import letter_grade, gpa, subject_average


class TestGradeCalculations(unittest.TestCase):

    def test_letter_grade_top_tier(self):
        """A score of 95/100 should return an 'A'."""
        self.assertEqual(letter_grade(95, 100), "A")

    def test_letter_grade_invalid_max_score(self):
        """A max_score <= 0 should raise ValueError."""
        with self.assertRaises(ValueError):
            letter_grade(50, 0)

    def test_gpa_empty_returns_none(self):
        """Calculating GPA on an empty list of grades should return None."""
        self.assertIsNone(gpa([]))

    def test_gpa_single_course(self):
        """Single course with score 95/100 should evaluate to 4.0 GPA."""
        grades = [{"student_id": "S1", "score": 95, "max_score": 100}]
        self.assertEqual(gpa(grades, "S1"), 4.0)

    def test_subject_average_single_entry(self):
        """A single grade entry for a subject should return that score as average."""
        grades = [{"subject": "Mathematics", "score": 85, "max_score": 100}]
        self.assertEqual(subject_average(grades, "Mathematics"), 85.0)

    def test_subject_average_nonexistent(self):
        """Subject average should return None if no entries exist for that subject."""
        self.assertIsNone(subject_average([], "Physics"))


if __name__ == "__main__":
    unittest.main()
