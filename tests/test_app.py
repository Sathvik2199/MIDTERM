import pytest
from app import App
from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand


# Test REPL behavior in the App class

def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as exit_exception:
        app.start()
    assert exit_exception.type == SystemExit


def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app=App()
    with pytest.raises(SystemExit):
        app.start()
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "Unknown command: unknown_command" in captured.out


# Test CommandHandler functionality with various commands

def test_register_and_execute_multiply_command(capsys):
    """Test registration and execution of the MultiplyCommand."""
    handler = CommandHandler()
    multiply_command = MultiplyCommand(6, 7)

    # Register the multiply command
    handler.register_command("multiply", multiply_command)

    # Execute the multiply command
    result = handler.execute_command("multiply")

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the output is correct
    assert captured.out == "MultiplyCommand: 6 * 7 = 42\n"
    assert result == 42


def test_register_and_execute_divide_command(capsys):
    """Test registration and execution of the DivideCommand."""
    handler = CommandHandler()
    divide_command = DivideCommand(10, 2)

    # Register the divide command
    handler.register_command("divide", divide_command)

    # Execute the divide command
    result = handler.execute_command("divide")

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the output is correct
    assert captured.out == "DivideCommand: 10 / 2 = 5.0\n"
    assert result == 5.0


def test_divide_by_zero():
    """Test that dividing by zero raises a ValueError."""
    handler = CommandHandler()
    divide_command = DivideCommand(10, 0)

    # Register the divide command
    handler.register_command("divide_zero", divide_command)

    # Check that dividing by zero raises the appropriate ValueError
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        handler.execute_command("divide_zero")


def test_register_and_execute_add_command(capsys):
    """Test registration and execution of the AddCommand."""
    handler = CommandHandler()
    add_command = AddCommand(2, 3)

    # Register the add command
    handler.register_command("add", add_command)

    # Execute the add command
    result = handler.execute_command("add")

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the output is correct
    assert captured.out == "AddCommand: 2 + 3 = 5\n"
    assert result == 5


def test_register_and_execute_subtract_command(capsys):
    """Test registration and execution of the SubtractCommand."""
    handler = CommandHandler()
    subtract_command = SubtractCommand(5, 2)

    # Register the subtract command
    handler.register_command("subtract", subtract_command)

    # Execute the subtract command
    result = handler.execute_command("subtract")

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the output is correct
    assert captured.out == "SubtractCommand: 5 - 2 = 3\n"
    assert result == 3


def test_execute_nonexistent_command():
    """Test executing a command that doesn't exist raises an error."""
    handler = CommandHandler()

    # Try executing a command that doesn't exist
    result = handler.execute_command("nonexistent")

    # Assert that the result matches the expected error message
    expected_message = "Unknown command: nonexistent"
    assert result == expected_message