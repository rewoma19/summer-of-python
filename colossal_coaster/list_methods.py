"""
    Functions to manage and organize queues at Chaitana's roller coaster.
"""

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """
        Add a person to the 'express' or 'normal' queue depending on the ticket number.

        :param express_queue: list - names in the Fast-track queue.
        :param normal_queue: list - names in the normal queue.
        :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
        :param person_name: str - name of person to add to a queue.
        :return: list - the (updated) queue the name was added to.
    """

    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    elif ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue