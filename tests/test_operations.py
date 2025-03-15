""" Unit tests for basic arithmetic operations using the Calculation class. """

from decimal import Decimal, getcontext, ROUND_HALF_UP
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

# Set precision and rounding mode for Decimal operations
getcontext().prec = 3
getcontext().rounding = ROUND_HALF_UP

def test_operation_add():
    """ Test the addition operation using the Calculation class. """
    calculation = Calculation(Decimal('15'), Decimal('7'), add)
    assert calculation.perform() == Decimal('22'), "Add operation failed"

def test_operation_subtract():
    """ Test the subtraction operation using the Calculation class. """
    calculation = Calculation(Decimal('15'), Decimal('7'), subtract)
    assert calculation.perform() == Decimal('8'), "Subtract operation failed"

def test_operation_multiply():
    """ Test the multiplication operation using the Calculation class. """
    calculation = Calculation(Decimal('15'), Decimal('7'), multiply)
    assert calculation.perform() == Decimal('105'), "Multiply operation failed"

def test_operation_divide():
    """ Test the division operation using the Calculation class. """
    calculation = Calculation(Decimal('15'), Decimal('7'), divide)
    result = calculation.perform()
    expected_result = Decimal('2.14').quantize(Decimal('0.01'))
    assert result == expected_result, (
        f"Divide operation failed: expected {expected_result}, got {result}" )

def test_divide_by_zero():
    """ Test division by zero handling using the Calculation class. """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('15'), Decimal('0'), divide)
        calculation.perform()