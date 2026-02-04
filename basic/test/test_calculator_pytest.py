import pytest
from calculator import square


#run "pytest test_calculator_pytest" instead of "python test_calculator_pytest"

#BASE version: run all the test at the same time
"""
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
"""

#COMPLETE version: all the function are run in this way I have more clue to identify the error 
# (normally it stops at the first error as in the BASE version) 
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0


#TEST: pytest.raises(TypeError) -> #Assert that a code block/function call raises an exception type, or one of its subclasses.
#TypeError is the type of expection that I expect
#the function raises allow to express that I expect an expection to be raised
def test_str():
    with pytest.raises(TypeError):
        square("cat") #Whenever I call square("cat"), I expect the TypeError to be raised