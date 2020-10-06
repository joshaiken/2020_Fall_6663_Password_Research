# Tester File for PasswordGenerator.py

from PasswordGenerator import *

#Test should fail
def test_badWord():
    assert validWordType("preposition")

#Test should pass
def test_sqrt2():
    assert validWordType("noun")