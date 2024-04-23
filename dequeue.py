# Dequeue


# A deque (double-ended queue) is a data structure
# that allows adding and removing elements from both ends, front and back.

class Dequeue:
    def __init__(self):
        """
        Initialize a dequeue object which is an empty list.
        """
        self.items = []

    def is_empty(self):
        """
        Checks if the dequeue object is empty.
        :return:
        """
        return self.items == []

    def append(self, item):
        """
        Append an item to the back of the dequeue.
        :param item:
        :return:
        """
        self.items.append(item)

    def append_left(self, item):
        """
        Append an item to the front of the dequeue.
        :param item:
        :return:
        """
        self.items.index(0, item)

    def pop(self):
        """
        Remove item from the back of the dequeue.
        :return:
        """
        if self.is_empty():
            raise IndexError('Dequeue is empty')
        self.items.pop()

    def pop_left(self):
        """
        Remove item from the front of the dequeue.
        :return:
        """
        if self.is_empty():
            raise IndexError('Dequeue is empty')
        self.items.pop(0)

    def size(self):
        """
        Return the size of the dequeue.
        :return:
        """
        return len(self.items)