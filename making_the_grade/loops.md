# Instructions

You're a teaching assistant correcting student exams. Keeping track of results manually is getting both tedious and mistake-prone. You decide to make things a little more interesting by putting together some functions to count and calculate results for the class.

## Task 1

### Rounding Scores

While you can give "partial credit" on exam questions, overall exam scores have to be **int**s. So before you can do anything else with the class scores, you need to go through the grades and turn any **float** scores into **int**s. Lucky for you, Python has the built-in **round()** function you can use.

Create the function **round_scores(student_scores)** that takes a **list** of **student_scores**. This function should consume the input **list** and **return** a new list with all the scores converted to **int**s. The order of the scores in the resulting **list** is not important.
