from app.commands import Command

class MultiplyCommand(Command):
    """Class to represent a multiplication command."""
    def _init_(self, a, b):
        """Initialize the command with two operands."""
        self.a = a
        self.b = b

    def execute(self):
        """Execute the multiplication command.
        """
        result = self.a * self.b
        print(f"MultiplyCommand: {self.a} * {self.b} = {result}")
        return result