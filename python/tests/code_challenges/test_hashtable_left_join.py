import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_left_join_no_right_is_none():
    left = {
        "apple": "banana",
        "pineapple": "coconut",
    }
    right = {
        "apple": "orange",
    }

    expected = [
        ["apple", "banana", "orange"],
        ["pineapple", "coconut", "NONE"],
    ]

    actual = left_join(left, right)
    assert sorted(actual) == sorted(expected)

# @pytest.mark.skip("TODO")
def test_left_join_right_is_empty():
    left = {
        "apple": "banana",
        "pineapple": "coconut",
    }
    right = {}

    expected = [
        ["apple", "banana", "NONE"],
        ["pineapple", "coconut", "NONE"],
    ]

    actual = left_join(left, right)
    assert sorted(actual) == sorted(expected)

# @pytest.mark.skip("TODO")
def test_left_join_no_left_ignores_right():
    left = {
        "apple": "banana",
    }
    right = {
        "apple": "orange",
        "pineapple": "coconut",
    }

    expected = [
        ["apple", "banana", "orange"],
    ]

    actual = left_join(left, right)
    assert sorted(actual) == sorted(expected)

# @pytest.mark.skip("TODO")
def test_left_join():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["fond", "enamored", "averse"],
        ["wrath", "anger", "delight"],
        ["diligent", "employed", "idle"],
        ["outfit", "garb", "NONE"],
        ["guide", "usher", "follow"],
    ]

    actual = left_join(synonyms, antonyms)
    assert sorted(actual) == sorted(expected)
