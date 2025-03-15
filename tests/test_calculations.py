from decimal import Decimal

from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

def test_add_calculation():
    """Test adding a new calculation to the history."""
    Calculations.clear_history()
    calc = Calculation(Decimal('1'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, (
        "The new calculation was not added to the history as expected."
    )

def test_get_history():
    """Test retrieving the calculation history."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('15'), Decimal('7'), add))
    Calculations.add_calculation(Calculation(Decimal('20.5'), Decimal('1.5'), subtract))
    history = Calculations.get_history()
    assert len(history) == 2, "The history does not contain the expected number of calculations."

def test_clear_history():
    """Test clearing the calculation history."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('15'), Decimal('7'), add))
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "The history was not cleared as expected."

def test_get_latest():
    """Test retrieving the latest calculation from the history."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('15'), Decimal('7'), add))
    Calculations.add_calculation(Calculation(Decimal('20.5'), Decimal('1.5'), subtract))
    latest = Calculations.get_latest()
    assert latest.a == Decimal('20.5') and latest.b == Decimal('1.5'), (
        "The latest calculation retrieved is incorrect."
    )

def test_find_by_operation():
    """Test finding calculations by operation name."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('15'), Decimal('7'), add))
    Calculations.add_calculation(Calculation(Decimal('20.5'), Decimal('1.5'), subtract))
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, (
        "The expected number of 'add' operations was not found in the history."
    )
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, (
        "The expected number of 'subtract' operations was not found in the history."
    )

def test_get_latest_with_empty_history():
    """Test retrieving the latest calculation when the history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, (
        "Expected None when retrieving the latest calculation from an empty history."
    )
    