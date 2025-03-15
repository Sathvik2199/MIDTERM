import os
import logging
from abc import ABC, abstractmethod
import pandas as pd

# Create the logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

class CalculationHistory:
    """Singleton class to manage calculation history."""    
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Create a new instance if it doesn't exist."""
        if not cls._instance:
            cls._instance = super(CalculationHistory, cls).__new__(cls)
        return cls._instance

    def __init__(self, filename='calculation_history.csv'):
        """Initialize the calculation history."""
        if not hasattr(self, 'initialized'):
            self.filename = filename
            self.history = pd.DataFrame(columns=['operation', 'operands', 'result'])
            if os.path.exists(self.filename):
                self.history = pd.read_csv(self.filename)
            self.initialized = True

    def add_entry(self, operation, operands, result):
        """Add a new entry to the calculation history."""
        new_entry = pd.DataFrame({
            'operation': [operation],
            'operands': [operands],
            'result': [result]
        })
        self.history = pd.concat([self.history, new_entry], ignore_index=True)
        self.save_history()

    def save_history(self):
        """Save the calculation history to a CSV file."""
        self.history.to_csv(self.filename, index=False)

    def clear_history(self):
        """Clear the calculation history."""
        self.history = pd.DataFrame(columns=['operation', 'operands', 'result'])
        self.save_history()

    def delete_entry(self, index):
        """Delete an entry from the calculation history."""
        if 0 <= index < len(self.history):
            self.history = self.history.drop(index).reset_index(drop=True)
            self.save_history()
        else:
            raise IndexError("Invalid index. Cannot delete entry.")

    def show_history(self):
        """Return the calculation history."""
        return self.history


class Command(ABC):
    """Abstract base class for commands."""

    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass


class AddCommand(Command):
    """Command to add two numbers."""

    def __init__(self, a, b):
        """Initialize with two operands."""
        self.a = a
        self.b = b

    def execute(self):
        """Perform addition."""
        return self.a + self.b


class SubtractCommand(Command):
    """Command to subtract two numbers."""

    def __init__(self, a, b):
        """Initialize with two operands."""
        self.a = a
        self.b = b

    def execute(self):
        """Perform subtraction."""
        return self.a - self.b


class MultiplyCommand(Command):
    """Command to multiply two numbers."""

    def __init__(self, a, b):
        """Initialize with two operands."""
        self.a = a
        self.b = b

    def execute(self):
        """Perform multiplication."""
        return self.a * self.b


class DivideCommand(Command):
    """Command to divide two numbers."""

    def __init__(self, a, b):
        """Initialize with two operands."""
        self.a = a
        self.b = b

    def execute(self):
        """Perform division."""
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b


class PowerCommand(Command):
    """Command to calculate the power of two numbers."""

    def __init__(self, base, exponent):
        """Initialize with base and exponent."""
        self.base = base
        self.exponent = exponent

    def execute(self):
        """Perform power operation."""
        return self.base ** self.exponent


class MenuCommand(Command):
    """Command to display available operations."""

    def execute(self):
        """Return a list of available operations."""
        return (
            "Available operations: add, subtract, multiply, divide, power, "
            "menu, history, clear, delete"
        )


class CommandHandler:
    """Class to handle command registration and execution."""

    def __init__(self):
        """Initialize the command handler."""
        self.commands = {}

    def register_command(self, operation, command):
        """Register a new command."""
        self.commands[operation] = command

    def execute_command(self, operation):
        """Execute a command if it exists."""
        if operation in self.commands:
            return self.commands[operation].execute()
        raise ValueError("Unknown operation.")


# Implementation of the Facade Pattern
class CalculationFacade:
    """Facade for calculation operations."""

    def __init__(self):
        """Initialize the facade with history and command handler."""
        self.history = CalculationHistory()
        self.handler = CommandHandler()

    def perform_operation(self, operation, a, b):
        """Perform the given operation with the provided operands."""
        command = self.create_command(operation, a, b)
        result = command.execute()
        self.history.add_entry(operation, (a, b), result)
        return result

    def create_command(self, operation, a, b):
        """Create and return the appropriate command object."""
        if operation == 'add':
            return AddCommand(a, b)
        if operation == 'subtract':
            return SubtractCommand(a, b)
        if operation == 'multiply':
            return MultiplyCommand(a, b)
        if operation == 'divide':
            return DivideCommand(a, b)
        if operation == 'power':  # New command for power operation
            return PowerCommand(a, b)
        raise ValueError("Unknown operation.")

    def show_history(self):
        """Show the calculation history."""
        return self.history.show_history()

    def clear_history(self):
        """Clear the calculation history."""
        self.history.clear_history()

    def delete_entry(self, index):
        """Delete an entry from the calculation history."""
        self.history.delete_entry(index)


def main():
    """Main function to run the calculator application."""
    facade = CalculationFacade()  # Use the Facade
    while True:
        operation = input("Enter operation (add, subtract, multiply, divide, power, menu, history, clear, delete) or 'quit' to exit: ")

        if operation == 'quit':
            logging.info("Exiting the app. Goodbye!")
            break

        if operation == 'menu':
            print("Available operations: add, subtract, multiply, divide, power, menu, history, clear, delete")
            logging.info("Displayed menu options.")
            continue

        if operation == 'history':
            print(facade.show_history())
            logging.info("Displayed calculation history.")
            continue

        if operation == 'clear':
            facade.clear_history()
            print("History cleared.")
            logging.info("Cleared calculation history.")
            continue

        if operation == 'delete':
            index = input("Enter the index of the entry to delete: ")
            try:
                index = int(index)
                facade.delete_entry(index)
                print(f"Entry at index {index} deleted.")
                logging.info(f"Deleted entry at index {index}.")
            except (ValueError, IndexError) as error:
                print(f"Error deleting entry: {error}")
                logging.error("Error deleting entry: %s", error)
            continue

        a = input("Enter first number: ")
        b = input("Enter second number: ")

        try:
            a = int(a)
            b = int(b)

            # Perform the operation via the facade
            result = facade.perform_operation(operation, a, b)
            print(f"The result is: {result}")
            logging.info("Executed %s command with result: %s", operation, result)

        except ValueError as error:
            logging.error("Invalid input: %s", error)
            print(f"Invalid input: {error}")


# Ensure the program starts correctly
if __name__ == "__main__":
    main()