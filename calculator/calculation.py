"""
This module defines the Calculation class. The Calculation class supports the creation of
calculation instances and executing the operation to obtain the result.
"""
from decimal import Decimal
from typing import Callable

class Calculation:
    """ Represents an arithmetic calculation involving two Decimal numbers."""

    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """ Initializes a Calculation object with two operands and an operation. """
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """ Factory method to create a new Calculation instance."""
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        """ Executes the operation on the two operands. """
        return self.operation(self.a, self.b)

    def __repr__(self) -> str:
        """ Returns a string representation of the Calculation instance. """
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"