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

