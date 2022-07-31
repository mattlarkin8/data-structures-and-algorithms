from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Data structure that stores values in linked nodes.
    Uses Last In Last Out (LILO) to access the nodes in the queue.
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        new_node = Node(val)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        old_front = self.front
        self.front = old_front.next
        return old_front.value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def is_empty(self):
        return self.front is None

class Node:
    def __init__(self, val, next_=None):
        self.value = val
        self.next = next_
