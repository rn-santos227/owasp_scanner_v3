import inquirer

from utils.clear_screen import clear_screen

sensitive_data_menu = [
  inquirer.List("choice",
    message = "Choose your Endpoint Activity",
    choices=[],
    carousel=True
  ),
]