from data_structures.queue import Queue


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def clone(self):
        if not self.root:
            return KaryTree()

        breadth = Queue()
        breadth.enqueue(self.root)
        clone_root = None
        while not breadth.is_empty():
            front = breadth.dequeue()
            clone_front = Node(front.value)

            if not clone_root:
                clone_root = clone_front

            for child in front.children:
                breadth.enqueue(child)
                clone_node = Node(child.value)
                clone_front.children.append(clone_node)

        return KaryTree(root=clone_root)

    def breadth_first(self):
        breadth = Queue()

        collection = []

        breadth.enqueue(self.root)

        while not breadth.is_empty():
            node = breadth.dequeue()
            collection.append(node.value)
            for child in node.children:
                breadth.enqueue(child)

        return collection


class Node:
    """K-Ary Tree Node"""

    def __init__(self, value, children=None):
        self.value = value
        self.children = [] if children is None else children

    def __str__(self):
        return str(self.value)
