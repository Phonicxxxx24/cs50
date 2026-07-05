from datetime import date
from season import get_minutes, minutes_to_words

def test_get_minutes():
    birth = date(2000, 1, 1)
    today = date(2000, 1, 2)  # 1 day later
    assert get_minutes(birth, today) == 1440  # 1 day = 1440 minutes

def test_minutes_to_words():
    assert minutes_to_words(1440) == "one thousand four hundred forty minutes"