class LinkedList:
    """
    Used to create a singly linked list. Has methods to create a new node at the beginning of the list, search
    for a value in the list, and return a string that represents all items in the list.
    """

    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        text = ""
        current = self.head
        while current is not None:
            text += "{ " + str(current.value) + " } -> "
            current = current.next

        return text + "NULL"

    def includes(self, val):
        current = self.head
        while current is not None:
            if current.value == val:
                return True
            current = current.next

        return False

class Node:
    def __init__(self, val, next = None):
        self.value = val
        self.next = next

class TargetError:
    pass
