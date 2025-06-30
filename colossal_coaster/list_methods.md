# Instructions

Chaitana owns a very popular theme park. She only has one ride in the very center of beautifully landscaped grounds: The Biggest Roller Coaster in the World(TM). Although there is only this one attraction, people travel from all over the world and stand in line for hours for the opportunity to ride Chaitana's hypercoaster.

There are two queues for this ride, each represented as a **list**:

1. Normal Queue

2. Express Queue (also known as the Fast-track) - where people pay extra for priority access.

You have been asked to write some code to better manage the guests at the park. You need to implement the following functions as soon as possible before the guests (and your boss, Chaitana!) get cranky. Make sure you read carefully. Some tasks ask that you change or update the existing queue, while others ask you to make a copy of it.

## Task 1

### Add me to the queue

Define the **add_me_to_the_queue()** function that takes 4 parameters **<express_queue>, <normal_queue>, <ticket_type>, <person_name>** and returns the appropriate queue updated with the person's name.

1. **<ticket_type>** is an **int** with 1 == express_queue and 0 == normal_queue.

2. **<person_name>** is the name (as a **str**) of the person to be added to the respective queue.

## Task 2

### Where are my friends?

One person arrived late at the park but wants to join the queue where their friends are waiting. But they have no idea where their friends are standing and there isn't any phone reception to call them.

Define the **find_my_friend()** function that takes 2 parameters **queue** and **friend_name** and returns the position in the queue of the person's name.

1. **queue** is the **list** of people standing in the queue.

2. **friend_name** is the name of the friend whose index (place in the queue) you need to find.

Remember: Indexing starts at 0 from the left, and -1 from the right.
