from app.commands import Command

class DivideCommand(Command):
    """Class to represent a division command."""
    def init(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")  # Raise ValueError for division by zero
        result = self.a / self.b
        print(f"DivideCommand: {self.a} / {self.b} = {result}")
        return result