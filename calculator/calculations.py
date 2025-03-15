""" This module manages a history of Calculation instances. """

from typing import List
from calculator.calculation import Calculation

class Calculations:
    """ A class to manage a history of Calculation instances. """
    _history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """ Adds a new calculation to the history. """
        cls._history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """ Returns the full history of calculations. """
        return list(cls._history)

    @classmethod
    def clear_history(cls):
        """ Clears the history of all calculations.  """
        cls._history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """ Returns the latest calculation added to the history. """
        return cls._history[-1] if cls._history else None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """ Finds all calculations that use a specific operation. """
        return [calc for calc in cls._history if calc.operation.__name__ == operation_name]