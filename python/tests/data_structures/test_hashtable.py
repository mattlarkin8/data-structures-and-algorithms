import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

# @pytest.mark.skip("TODO")
def test_buckets_size():
    table = Hashtable()
    actual = len(table.buckets)
    expected = 1024
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_hash_in_range():
    table = Hashtable(size=2)
    keys = ["spam", "eggs", "bacon"]
    for key in keys:
        index = table.hash(key)
        assert 0 <= index <= table.size

# @pytest.mark.skip("TODO")
def test_set_creates_new_entry():
    table = Hashtable()
    table.set("spam", "eggs")
    assert True

# @pytest.mark.skip("TODO")
def test_set_repeat_key():
    table = Hashtable()
    table.set("spam", "eggs")
    table.set("spam", "bacon")
    actual = table.get("spam")
    expected = "bacon"
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_contains():
    table = Hashtable()
    table.set("spam", "eggs")
    actual = table.contains("spam")
    expected = True
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_not_contains():
    table = Hashtable()
    table.set("spam", "eggs")
    actual = table.contains("bacon")
    expected = False
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_keys():
    table = Hashtable()
    table.set("spam", "eggs")
    table.set("eggs", "bacon")
    keys = table.keys()
    actual = sorted(keys)
    expected = ["eggs", "spam"]
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_get_returns_none_for_missing_key():
    table = Hashtable()
    actual = table.get("test")
    expected = None
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_get_returns_value_given_key():
    table = Hashtable()
    table.set("test", "Test value")
    actual = table.get("test")
    expected = "Test value"
    assert actual == expected
