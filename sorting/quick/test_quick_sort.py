import pytest
from quick_sort import quick_sort

# @pytest.mark.skip("pending")
def test_merge_sort():
    actual = quick_sort([8,4,23,42,16,15], 0, 5)
    expected = [4,8,15,16,23,42]
    assert actual == expected

@pytest.mark.skip("pending")
def test_merge_sort_reverse():
    actual = quick_sort([20,18,12,8,5,-2], 0, 5)
    expected = [-2,5,8,12,18,20]
    assert actual == expected

@pytest.mark.skip("pending")
def test_merge_sort_few_unique():
    actual = quick_sort([5,12,7,5,5,7], 0, 5)
    expected = [5,5,5,7,7,12]
    assert actual == expected

@pytest.mark.skip("pending")
def test_merge_sort_nearly_sorted():
    actual = quick_sort([2,3,5,7,13,11], 0, 5)
    expected = [2,3,5,7,11,13]
    assert actual == expected

@pytest.mark.skip("pending")
def test_merge_sort_sorted():
    actual = quick_sort([2,3,5,7,11,13], 0, 5)
    expected = [2,3,5,7,11,13]
    assert actual == expected

# @pytest.mark.skip("pending")
def test_merge_sort_empty():
    actual = quick_sort([],0,0)
    expected = []
    assert actual == expected

