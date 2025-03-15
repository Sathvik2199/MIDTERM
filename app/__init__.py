import pkgutil
import importlib
from app.commands import CommandHandler, Command

class App:
    """A class to manage the application, including loading commands and executing user inputs."""

    def __init__(self):
        """Initialize the command handler."""
        self.command_handler = CommandHandler()

    def load_plugins(self):
        """Dynamically load all plugins in the plugins directory and register them with the command handler."""
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command):  # Assuming a Command base class exists
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        pass  # item was not a class or was not a subclass of Command

    def start(self):
        """Start the application and process user commands."""
        self.load_plugins()
        while True:
            user_input = input("Enter a command (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                raise SystemExit("Exiting app.")
            result = self.command_handler.execute_command(user_input)
            if result is None:
                print(f"No such command: {user_input}")
            else:
                print(result)