import pytest
from twttr import shorten

def test_basic():
    assert shorten("Harshit") == "Hrsht"
def test_vowels():
    assert shorten("AEIOU")== ""
def test_novowels():
    assert shorten("HHH") == "HHH"
def test_empty():
    assert shorten("") == ""
