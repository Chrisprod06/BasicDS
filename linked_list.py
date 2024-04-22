# Linked list

# A linked list is a data structure where elements are linked together in a linear fashion. Each element, or node,
# contains a data value and a reference (link) to the next node in the list. The first node is called the head,
# and the last node has a reference to None, indicating the end of the list.


# Node: Represents a single element in the list. It contains data and a reference to the next node.
# LinkedList: Manages the list. It keeps a reference to the head node and provides methods to manipulate the list.

class Node:
    def __init__(self, data):
        """
        Initializes a Node. It holds the data and the next node. Initially the Node referenced to nothing
        :param data:
        """
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        """
        Initializes the Linked List. At first the head references nothing
        """
        self.head = None

    def is_empty(self):
        """
        Checks if Linked List is empty or not
        :return:
        """
        return True if not self.head else False

    def append(self, data):
        """
        Create a node and add it at the end of the Linked List.
        :return:
        """
        # Create a new node with the given data
        new_node = Node(data)
        # if the list is empty, set it as head
        if self.is_empty():
            self.head = new_node
        # if it's not empty, traverse to the end and append the new node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        """
        Create a node and add it at the beginning of the Linked List.
        :param data:
        :return:
        """
        # Create a new node
        new_node = Node(data)
        # Set next to reference the head
        new_node.next = self.head
        # Make the new node the head of the linked list
        self.head = new_node

    def delete(self, data):
        """
        Find the node with the given data in the Linked List and delete it.
        :param data:
        :return:
        """
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next

        if not current:
            return  # Data not found in the list

        if previous:
            previous.next = current.next
        else:
            # Deleting the head node
            self.head = current.next

    def display(self):
        """
        Prints the Linked List
        :return:
        """
        # Display the linked list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
