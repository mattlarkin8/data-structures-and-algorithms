from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)

        if not self.root:
            self.root = node
            return

        def walk(root, new_node):
            if root is None:
                return

            if new_node.value < root.value:
                if not root.left:
                    root.left = new_node
                else:
                    walk(root.left, new_node)
            else:
                if not root.right:
                    root.right = new_node
                else:
                    walk(root.right, new_node)

        walk(self.root, node)


    def contains(self, target):

        def walk(root):
            if root is None:
                return False

            if root.value == target:
                return True

            if target < root.value:
                return walk(root.left)
            else:
                return walk(root.right)

        return walk(self.root)
