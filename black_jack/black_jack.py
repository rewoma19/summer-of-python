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