from cards import Card
import pytest

def assert_identical(c1: Card, c2: Card):
    __tracebackhide__ = True # hide this helper function from tracebacks
    assert c1 == c2 # check whether all fields are identical except for id.
    if c1.id != c2.id: # check whether the ids are identical
        pytest.fail(f"ids do not match: {c1.id} != {c2.id}")

def test_identical():
    c1 = Card("foo", id=123)
    c2 = Card("foo", id=123)
    assert_identical(c1, c2)

def test_identical_fail():
    c1 = Card("foo", id=123)
    c2 = Card("foo", id=456)
    with pytest.raises(AssertionError):
        assert_identical(c1, c2)