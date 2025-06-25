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

def list_contains_round(rounds, number):
    """
        Check if the list of rounds contains the specified number.

        :param rounds: list - rounds played.
        :param number: int - round number.
        :return: bool - was the round played?
    """

    contains_round = number in rounds
    return contains_round

def card_average(hand):
    """
        Calculate and return the average card value from the list

        :param hand: list - cards in hand.
        :return: float - average value of the cards in the hand.
    """

    num_of_cards = len(hand)
    sum_of_cards = sum(hand)

    average_of_cards = sum_of_cards / num_of_cards
    return average_of_cards