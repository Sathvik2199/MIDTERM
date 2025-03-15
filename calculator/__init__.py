"""
This module initializes the Calculator package, main Calculator class
and handles the primary arithmetic operations including addition, subtraction,
multiplication, and division. It also manages the calculation history.
"""
from decimal import Decimal
from typing import Callable

from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

class Calculator:
    "Calculator class"
    @staticmethod
    def _operate(a: Decimal, b: Decimal, func: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calc = Calculation.create(a, b, func)
        Calculations.add_calculation(calc)
        return calc.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """ Returns the sum of two Decimal numbers. """
        return Calculator._operate(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """ Returns the difference between two Decimal numbers. """
        return Calculator._operate(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """ Returns the product of two Decimal numbers. """
        return Calculator._operate(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """ Returns the quotient of two Decimal numbers. """
        return Calculator._operate(a, b, divide)