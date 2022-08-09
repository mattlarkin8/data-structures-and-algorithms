import pytest
from data_structures.binary_tree import BinaryTree, Node
from data_structures.invalid_operation_error import InvalidOperationError


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_max_val_zero():
    tree = BinaryTree()
    tree.root = Node(-27)
    tree.root.left = Node(0)
    tree.root.right = Node(-5)

    actual = tree.find_maximum_value()
    expected = 0

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_max_val_empty():
    tree = BinaryTree()
    with pytest.raises(InvalidOperationError):
        tree.find_maximum_value()
