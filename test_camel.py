from camel_case import checks

def test_convert():
    assert checks("jainHarshit") == "jain_harshit"
    assert checks("isHappy") == "is_happy"


