class LinkedList:
    """
    Used to create a singly linked list. Has methods to create a new node at the beginning of the list, search
    for a value in the list, and return a string that represents all items in the list.
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        text = ""
        current = self.head
        while current is not None:
            text += "{ " + str(current.value) + " } -> "
            current = current.next

        return text + "NULL"

    def insert(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def insert_before(self, idx, new):
        if self.head is None:
            raise TargetError

        current = self.head
        if current.value == idx:
            new_node = Node(new)
            new_node.next = self.head
            self.head = new_node
            return f"Successfully created {new}!"

        while current is not None:
            if current.next.value == idx:
                new_node = Node(new)
                new_node.next = current.next
                current.next = new_node
                return f"Successfully created {new}!"
            current = current.next

        raise TargetError

    def insert_after(self, idx, new):
        if self.head is None:
            raise TargetError

        current = self.head
        while current is not None:
            if current.value == idx:
                new_node = Node(new)
                new_node.next = current.next
                current.next = new_node
                return f"Successfully created {new}!"
            current = current.next


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

class TargetError(Exception):
    pass
