"""
    Functions for organizing and calculating student exam scores.
"""

def round_scores(student_scores):
    """
        Round all provided student scores.

        :param student_scores: list - float or int of student exam scores.
        :return: list - student scores *rounded* to nearest integer value.
    """
    rounded_scores = []

    for score in student_scores:
        rounded_score = round(score)
        rounded_scores.append(rounded_score)

    return rounded_scores

def count_failed_students(student_scores):
    """
        Count the number of failing students out of the group provided.

        :param student_scores: list - containing int student scores.
        :return: int - count of student scores at or below 40.
    """

    students_with_failed_grade = 0

    for score in student_scores:
        if score <= 40:
            students_with_failed_grade += 1

    return students_with_failed_grade

