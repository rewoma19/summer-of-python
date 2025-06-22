# Instructions

In this exercise, you are going to implement some rules of **Blackjack**, such as the way the game is played and scored.

**Note**: In this exercise, **A**, means ace, **J** means jack, **Q** means queen, and **K** means king. Jokers are discarded. A **standard French-suited 52-card deck** is assumed, but in most versions, several decks are shuffled together for play.

## Task 1

### Calculate the value of a card

In Blackjack, it is up to each individual player if an ace is worth 1 or 11 points (more on that later). Face cards (**J**, **Q**, **K**) are scored at 10 points and any other card is worth its "pip" (numerical) value.

Define the **value_of_card(<card>)** function with parameter **card**. The function should return the numerical value of the passed-in card string. Since an ace can take on multiple values (1 **or** 11), this function should fix the value of an ace card at 1 for the time being. Later on, you will implement a function to determine the value of an ace card, given an existing hand.
