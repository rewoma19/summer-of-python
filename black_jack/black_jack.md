# Instructions

In this exercise, you are going to implement some rules of **Blackjack**, such as the way the game is played and scored.

**Note**: In this exercise, **A**, means ace, **J** means jack, **Q** means queen, and **K** means king. Jokers are discarded. A **standard French-suited 52-card deck** is assumed, but in most versions, several decks are shuffled together for play.

## Task 1

### Calculate the value of a card

In Blackjack, it is up to each individual player if an ace is worth 1 or 11 points (more on that later). Face cards (**J**, **Q**, **K**) are scored at 10 points and any other card is worth its "pip" (numerical) value.

Define the **value_of_card(<card>)** function with parameter **card**. The function should return the numerical value of the passed-in card string. Since an ace can take on multiple values (1 **or** 11), this function should fix the value of an ace card at 1 for the time being. Later on, you will implement a function to determine the value of an ace card, given an existing hand.

## Task 2

### Determine which card has a higher value

Define **higher_card(<card_one>, <card_two>)** function having parameters **card_one** and **card_two**. For scoring purposes, the value of **J**, **Q**, or **K** is 10. The function should return which card has the higher value for scoring. If both cards have an equal value, return both. Returning both cards can be done by using a comma in the **return** statement.

> # Using a comma in a return creates a Tuple. Tuples will be covered in a later exercise.

An ace can take on multiple values, so we will fix **A** cards to a value of 1 for this task.
