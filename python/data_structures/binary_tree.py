from data_structures.invalid_operation_error import InvalidOperationError

class BinaryTree:
    """
    Data structure that stores values in nodes.
    Nodes are linked together to form a tree.
    Each node has a left and right link.
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        values = []

        def walk(root):
            if root is None:
                return
            values.append(root.value)
            walk(root.left)
            walk(root.right)

        walk(self.root)
        return values

    def in_order(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        values = []

        def walk(root):
            if root is None:
                return
            walk(root.left)
            values.append(root.value)
            walk(root.right)

        walk(self.root)
        return values

    def post_order(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        values = []

        def walk(root):
            if root is None:
                return
            walk(root.left)
            walk(root.right)
            values.append(root.value)

        walk(self.root)
        return values

    def find_maximum_value(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        max_value = None

        def walk(root):
            nonlocal max_value

            if root is None:
                return
            if max_value is None:
                max_value = root.value
            if root.value > max_value:
                max_value = root.value
            walk(root.left)
            walk(root.right)

        walk(self.root)
        return max_value

    def is_empty(self):
        return self.root is None

class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.value = val

