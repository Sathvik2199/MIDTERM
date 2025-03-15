""" This module provides basic arithmetic operations for Decimal numbers. """

from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    """ Returns the sum of two Decimal numbers.  """
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """  Returns the difference between two Decimal numbers.  """
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """ Returns the product of two Decimal numbers. """
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """ Returns the quotient of two Decimal numbers. """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b