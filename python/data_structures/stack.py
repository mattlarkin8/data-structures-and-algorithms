from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Data structure that stores values in linked nodes.
    Uses Last In First Out (LIFO) to access the nodes in the stack.
    """

    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        old_top = self.top
        self.top = old_top.next
        return old_top.value

    def peek(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        return self.top is None

class Node:
    def __init__(self, val, next_=None):
        self.value = val
        self.next = next_
