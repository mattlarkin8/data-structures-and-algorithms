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

        while current and current.next is not None:
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
        raise TargetError

    def includes(self, val):
        current = self.head
        while current is not None:
            if current.value == val:
                return True
            current = current.next
        return False

    def get_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def kth_from_end(self, k):
        # raise error if k is under range
        if k < 0:
            raise TargetError

        # get length of list
        length = self.get_length()

        # raise error if k is larger than list
        if k >= length:
            raise TargetError

        # find index of target value
        target_idx = (length - 1) - k
        # set counter to track our index as we iterate
        current_idx = 0
        current = self.head
        # iterate through list
        while current:
            # check if we are at the correct index for our target
            if current_idx == target_idx:
                # return the target value upon reaching target
                return current.value
            # increment our index and move to next node
            current_idx += 1
            current = current.next

class Node:
    def __init__(self, val, next = None):
        self.value = val
        self.next = next

class TargetError(Exception):
    pass
