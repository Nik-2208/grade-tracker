"""Calculation module for academic grades, GPA, and averages."""

GRADE_POINTS = {
    "A": 10.0,
    "B": 9.0,
    "C": 8.0,
    "D": 7.0,
    "F": 0.0,
}


def letter_grade(score, max_score=100):
    """Determines the letter grade corresponding to a score and max_score."""
    if max_score <= 0:
        raise ValueError("max_score must be greater than 0")

    pct = (score / max_score) * 100

    if pct >= 90:
        return "A"
    elif pct >= 80:
        return "B"
    elif pct >= 70:
        return "C"
    elif pct >= 60:
        return "D"
    else:
        return "F"


def sgpa(grades, student_id=None, semester=None):
    """Calculates Semester Grade Point Average on a 10.0 scale."""
    if student_id is not None:
        grades = [g for g in grades if g.get("student_id") == student_id]
    if semester is not None:
        grades = [g for g in grades if str(g.get("semester", "")) == str(semester)]

    if not grades:
        return None

    total_points = 0.0
    total_credits = 0.0
    for g in grades:
        c = g.get("credits", 1.0)
        pts = GRADE_POINTS.get(letter_grade(g["score"], g["max_score"]), 0.0)
        total_points += pts * c
        total_credits += c

    if total_credits == 0:
        return 0.0
    return round(total_points / total_credits, 2)


def cgpa(grades, student_id=None):
    """Calculates Cumulative Grade Point Average on a 10.0 scale."""
    if student_id is not None:
        grades = [g for g in grades if g.get("student_id") == student_id]

    if not grades:
        return None

    total_points = 0.0
    total_credits = 0.0
    for g in grades:
        c = g.get("credits", 1.0)
        pts = GRADE_POINTS.get(letter_grade(g["score"], g["max_score"]), 0.0)
        total_points += pts * c
        total_credits += c

    if total_credits == 0:
        return 0.0
    return round(total_points / total_credits, 2)


def subject_average(grades, subject):
    """Calculates the average score for a given subject.

    Returns None if no entries exist for the subject.
    """
    matching = [
        g
        for g in grades
        if g.get("subject", "").strip().lower() == subject.strip().lower()
    ]
    if not matching:
        return None

    raw_scores = [g["score"] for g in matching]
    return round(sum(raw_scores) / len(raw_scores), 2)
