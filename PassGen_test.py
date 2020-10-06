# Tester File for PasswordGenerator.py

import math 

#Test should fail
def test_sqrt():
    num = 44
    assert math.sqrt(num) == 7

#Test should pass
def test_sqrt2():
    num=49
    assert math.sqrt(num) == 7