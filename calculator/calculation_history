import pandas as pd
import os

class CalculationHistory:
    """A class to manage the calculation history, storing operations, operands, and results."""

    def __init__(self, filename='calculation_history.csv'):
        """Initialize the CalculationHistory with a filename and load existing history if it exists."""
        self.filename = filename
        self.history = pd.DataFrame(columns=['operation', 'operands', 'result'])

        # Load existing history if the file exists
        if os.path.exists(self.filename):
            self.history = pd.read_csv(self.filename)

    def add_entry(self, operation, operands, result):
        """Add a new entry to the calculation history."""
        # Store operands as a string
        operands_str = str(operands)  # Convert tuple to string
        new_entry = pd.DataFrame({'operation': [operation], 'operands': [operands_str], 'result': [result]})
        self.history = pd.concat([self.history, new_entry], ignore_index=True)

    def save_history(self):
        """Save the current history to a CSV file."""
        self.history.to_csv(self.filename, index=False)

    def clear_history(self):
        """Clear the calculation history."""
        self.history = pd.DataFrame(columns=['operation', 'operands', 'result'])

    def show_history(self):
        """Return the current calculation history as a DataFrame."""
        return self.history