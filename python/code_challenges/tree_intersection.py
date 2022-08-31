from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable

def tree_intersection(btree1, btree2):
    table = Hashtable()
    matches = []

    def walk(root, do_something):
        if root is None:
            return
        do_something(root)
        walk(root.left, do_something)
        walk(root.right, do_something)

    def add_to_hashtable(root):
        table.set(str(root.value), root.value)

    def add_matches(root):
        if table.contains(str(root.value)) and root.value not in matches:
            matches.append(root.value)

    walk(btree1.root, add_to_hashtable)
    walk(btree2.root, add_matches)

    return matches
