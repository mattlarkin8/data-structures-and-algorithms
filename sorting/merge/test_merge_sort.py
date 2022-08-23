import pytest
from merge_sort import merge_sort

# @pytest.mark.skip("pending")
def test_merge_sort():
    actual = merge_sort([8,4,23,42,16,15])
    expected = [4,8,15,16,23,42]
    assert actual == expected

# @pytest.mark.skip("pending")
def test_merge_sort_reverse():
    actual = merge_sort([20,18,12,8,5,-2])
    expected = [-2,5,8,12,18,20]
    assert actual == expected

# @pytest.mark.skip("pending")
def test_merge_sort_few_unique():
    actual = merge_sort([5,12,7,5,5,7])
    expected = [5,5,5,7,7,12]
    assert actual == expected

# @pytest.mark.skip("pending")
def test_merge_sort_nearly_sorted():
    actual = merge_sort([2,3,5,7,13,11])
    expected = [2,3,5,7,11,13]
    assert actual == expected

# @pytest.mark.skip("pending")
def test_merge_sort_sorted():
    actual = merge_sort([2,3,5,7,11,13])
    expected = [2,3,5,7,11,13]
    assert actual == expected

# @pytest.mark.skip("pending")
def test_merge_sort_empty():
    actual = merge_sort([])
    expected = []
    assert actual == expected

# @pytest.mark.skip("pending")
def test_merge_sort_string():
    actual = merge_sort(["b","d","j","r","a","c"])
    expected = ["a","b","c","d","j","r"]
    assert actual == expected

# @pytest.mark.skip("pending")
def test_merge_sort_words():
    actual = merge_sort(["dog","cat","bear","ant","monkey"])
    expected = ["ant","bear","cat","dog","monkey"]
    assert actual == expected
