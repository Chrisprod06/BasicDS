# Stack implementation using list

# Explanation

# In Python, a stack is a data structure that follows the Last In, First Out (LIFO) principle
# , which means that the last element added to the stack is the first one to be removed.
# It's like a stack of plates—when you add a plate, it goes on top, and when you take a plate,
# you take the one from the top.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        Method used to add item at the end of the list (top)
        :param item:
        :return:
        """
        self.stack.append(item)

    def pop(self):
        """
        Method used to remove item at the end of the list (top)
        :return:
        """
        if not self.is_empty():
            return self.stack.pop(-1)
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        """
        Method used to check if stack is empty
        :return:
        """
        return True if len(self.stack) == 0 else False

    def size(self):
        """
        Method used to return the size of the stack
        :return:
        """
        return len(self.stack)

    def peek(self):
        """
        Method used to return the top item of the stack
        :return:
        """
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def print_stack(self):
        """
        Method used to print the stack
        :return:
        """
        print(self.stack)

