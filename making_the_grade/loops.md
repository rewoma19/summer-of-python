# Instructions

You're a teaching assistant correcting student exams. Keeping track of results manually is getting both tedious and mistake-prone. You decide to make things a little more interesting by putting together some functions to count and calculate results for the class.

## Task 1

### Rounding Scores

While you can give "partial credit" on exam questions, overall exam scores have to be **int**s. So before you can do anything else with the class scores, you need to go through the grades and turn any **float** scores into **int**s. Lucky for you, Python has the built-in **round()** function you can use.

Create the function **round_scores(student_scores)** that takes a **list** of **student_scores**. This function should consume the input **list** and **return** a new list with all the scores converted to **int**s. The order of the scores in the resulting **list** is not important.

## Task 2

### Non-Passing Students

As you were grading the exam, you noticed some students weren't performing as well as you had hoped. But you were distracted, and forgot to note exactly how many students.

Create the function **count_failed_students(student_scores)** that takes a **list** of **student_scores**. This function should count up the number of student who dont't have passing scores and return that count as an integer. A student needs a score greater than **40** to achieve a passing grade on the exam.

## Task 3

### The "Best"

The teacher you're assisting wants to find the group of students who've performed "the best" on this exam. What qualifies as "the best" fluctuates, so you need to find the student scores that are **greater than or equal to** the current threshold.

Create the function **above_threshold(student_scores, threshold)** taking **student_scores** (a **list** of grades), and **threshold** (the "top score" threshold) as parameters. This function should return a **list** of all scores that are **>=** to threshold.

## Task 4

### Calculating Letter Grades

The teacher you are assisting likes to assign letter grades as well as numeric scores. Since students rarely score 100 on an exam, the "letter grade" lower thresholds are calculated based on the highest score achieved, and increment evenly between the high score and the failing threshold of **<= 40**.

Create the function **letter_grades(highest)** that takes the "highest" score on the exam as an argument, and returns a **list** of lower score thresholds for each "American style" grade interval:
**["D", "C", "B", "A"]**
