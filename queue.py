# Queue


# A queue is a data structure that follows the First-In-First-Out (FIFO) principle,
# where the first element added to the queue is the first to be removed.

class Queue:
    def __init__(self):
        """
        At first a queue is an empty list.
        """
        self.items = []

    def is_empty(self):
        """
        Checks if the queue is empty.
        :return:
        """
        return len(self.items) == 0

    def enqueue(self, item):
        """
        Add a new item at the rear of the queue.
        :param item:
        :return:
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove the first item from the queue.
        :return:
        """
        if self.is_empty():
            raise IndexError('Queue is empty')
        self.items.pop(0)

    def peek(self):
        """
        Return the first item from the queue.
        :return:
        """
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.items[0]

    def size(self):
        """
        Return the size of the queue.
        :return:
        """
        return len(self.items)
