from data_structures.queue import Queue

def breadth_first(tree):
    values = []

    if tree.root is None:
        return values

    breadth = Queue()
    breadth.enqueue(tree.root)

    while not breadth.is_empty():
        root = breadth.dequeue()
        values.append(root.value)
        if root.left:
            breadth.enqueue(root.left)
        if root.right:
            breadth.enqueue(root.right)

    return values
