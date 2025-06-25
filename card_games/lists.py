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

def concatenate_rounds(rounds_1, rounds_2):
    """
        Concatenate two lists of round numbers.

        :param rounds_1: list - first rounds played.
        :param rounds_2: second dset of rounds played.
        :return: list - all rounds played.
    """

    all_rounds = rounds_1 + rounds_2
    return all_rounds