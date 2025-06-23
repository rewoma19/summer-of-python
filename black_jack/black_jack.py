"""
    Functions to help play and score a game of blackjack.
"""

def value_of_card(card):
    """
        Determine the scoring value of a card.

        :param card: str - given card.
        :return: int - value of a given card. See below for values.

        1. 'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2. 'A' (ace card) = 1
        3. '2' - '10' = numerical value.
    """

    face_cards = ['J', 'Q', 'K']
    ace_card = 'A'

    card_value = None

    if card in face_cards:
        card_value = 10
    elif card == ace_card:
        card_value = 1
    else:
        card_value = int(card)

    return card_value

def higher_card(card_one, card_two):
    """
        Determine which card has a higher value in the hand.

        :param card_one, card_two: str - cards dealt in hand. See below for values.
        :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

        1. 'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2. 'A' (ace card) = 1
        3. '2' - '10' = numerical value
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value > card_two_value:
        return card_one
    elif card_one_value == card_two_value:
        return card_one, card_two
    else:
        return card_two
    

def value_of_ace(card_one, card_two):
    """
        Calculate the most advantageous value for the ace card.

        :param card_one, card_two: str - card dealt. See below for values.
        :return: int - either 1 or 11 value of the upcoming ace card.

        1. 'J', 'Q', or 'K' (otherwise) known as "face cards") = 10
        2. 'A' (ace card) = 11 (if already in hand)
        3. '2' - '10' = numerical value.
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    value_of_both_cards = card_one_value + card_two_value

    ace_value = None

    if value_of_both_cards >= 11 or card_one == 'A' or card_two == 'A':
        ace_value = 1
    else:
        ace_value = 11

    return ace_value

def is_blackjack(card_one, card_two):
    """
        Determine if the hand is a 'natural' or 'blackjack'.

        :param card_one, card_two: str - card dealt. See below for values.
        :return: bool - if the hand is a blackjack (two cards worth 21).

        1. 'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2. 'A' (ace card) = 11 (if already in hand)
        3. '2' - '10' = numerical value.
    """

    is_blackjack_hand = False
    player_hand = [card_one, card_two]
    ten_cards = {'10', 'J', 'K', 'Q'}

    is_ace_in_hand = 'A' in player_hand
    is_ten_card_in_hand = card_one in ten_cards or card_two in ten_cards

    if is_ace_in_hand and is_ten_card_in_hand:
        is_blackjack_hand = True

    return is_blackjack_hand