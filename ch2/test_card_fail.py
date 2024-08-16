from cards import Card

def test_equality_fail(): # use $ pytest -vv test_card_fail.py to see the detailed traceback.
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "okken")
    assert c1 == c2