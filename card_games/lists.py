"""
    Functions for tracking poker hands and assorted card tasks.
"""

def get_round(number):
    """
        Create a list containing the current and next two round numbers.

        :param number: int - current round number.
        :return: list - current round and the two that follow.
    """

    poker_rounds = list()
    current_round = number

    while len(poker_rounds) < 3:
        poker_rounds.append(current_round)
        current_round += 1

    return poker_rounds