import pytest
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.menu import MenuCommand


# Test for AddCommand
def test_add_command():
    add_command = AddCommand(3, 5)
    assert add_command.execute() == 8

# Test for SubtractCommand
def test_subtract_command():
    subtract_command = SubtractCommand(10, 4)
    assert subtract_command.execute() == 6

# Test for MultiplyCommand
def test_multiply_command():
    multiply_command = MultiplyCommand(6, 7)
    assert multiply_command.execute() == 42

# Test for DivideCommand
def test_divide_command():
    divide_command = DivideCommand(20, 5)
    assert divide_command.execute() == 4

# Test for DivideCommand handling division by zero
def test_divide_by_zero():
    # Attempt to create a DivideCommand with a denominator of zero
    divide_command = DivideCommand(10, 0)  # Create an instance

    # Check that executing this command raises the expected ValueError
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_command.execute()  # This should raise the ValueError

# Test for MenuCommand
def test_menu_command():
    # Create a MenuCommand instance
    menu_command = MenuCommand()
    # Execute the command
    output = menu_command.execute()
    # Verify the expected output directly from the command
    expected_output = "Available operations: add, subtract, multiply, divide\n"  # This should match the command's output
    assert output == expected_output  # Check the output of the command