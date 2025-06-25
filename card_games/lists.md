# Instructors

Elyse is really looking forward to playing some poker (and other card games) during her upcoming trip to Vegas. Being a big fan of "self-tracking", she wants to put together some small functions that will help her with tracking tasks and has asked for your help thinking them through.

## Task 1

### Tracking Poker Rounds

Elyse is especially fond of poker, and wants to track how many rounds she plays - and which rounds those are. Every round has its own number, and every table shows the round number currently being played. Elyse chooses a table and sits down to play her first round. She plans on playing three rounds.

Implement a function **get_rounds(<round_number>)** that takes the current round number and returns a single **list** with that round and the next two that are coming up:

## Task 2

### Keeping all Rounds in the same place

Elyse played a few rounds at the first table, then took a break and played some more rounds at a second table ... but ended up with a different list for each table! She wants to put the two lists together, so she can track all of the poker rounds in the same place.

Implement a function **concatenate_rounds(<rounds_1>, <rounds_2>)** that takes two lists and returns a single **list** consisting of all the rounds in the first **list**, followed by all the rounds in the second **list**

## Task 3

### Finding Prior Rounds

Talking about some of the prior Poker rounds, another player remarks how similarly two of them played out. Elyse is not sure if she played those rounds or not.

Implement a function **list_contains_round(<rounds>, <round_number>)** that takes two arguments, a list of rounds played and a round number. The function will return **True** if the round is in the list of rounds played, **False** if not:
