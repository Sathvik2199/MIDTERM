'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    """ Test the addition method of the Calculator class. """
    assert Calculator.add(1, 2) == 3

def test_subtraction():
    """ Test the subtraction method of the Calculator class. """
    assert Calculator.subtract(1, 2) == -1

def test_divide():
    """ Test the division method of the Calculator class. """
    assert Calculator.divide(1, 2) == 0.5

def test_multiply():
    """ Test the multiplication method of the Calculator class. """
    assert Calculator.multiply(1, 2) == 2