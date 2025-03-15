from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a_value, b_value, operation, expected_output", [
    (Decimal('15'), Decimal('7'), add, Decimal('22')),
    (Decimal('15'), Decimal('7'), subtract, Decimal('8')),
    (Decimal('15'), Decimal('7'), multiply, Decimal('105')),
    (Decimal('16'), Decimal('4'), divide, Decimal('4')),
    (Decimal('20.5'), Decimal('1.5'), add, Decimal('22.0')),
    (Decimal('20.5'), Decimal('1.5'), subtract, Decimal('19.0')),
    (Decimal('20.5'), Decimal('3'), multiply, Decimal('61.5')),
    (Decimal('20'), Decimal('0.4'), divide, Decimal('50')),
])
def test_calculation_operations(a_value, b_value, operation, expected_output):
    """ Test various arithmetic operations using the Calculation class. """
    calc = Calculation(a_value, b_value, operation)
    result = calc.perform()
    assert result == expected_output, (
        f"Failed {operation._name_} operation with {a_value} and {b_value}: "
        f"expected {expected_output}, got {result}"
    )

def test_calculation_repr():
    """ Test the string representation of a Calculation instance. """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, f"Expected {expected_repr}, but got {repr(calc)}"

def test_divide_by_zero():
    """ Test division by zero handling. """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()