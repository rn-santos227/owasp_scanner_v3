import inquirer

from helpers.file_reader import file_reader
from utils.clear_screen import clear_screen

sensitive_data_menu = [
  inquirer.List("choice",
    message = "Choose your Endpoint Activity",
    choices=[],
    carousel=True
  ),
]

def count_sensitive_data():
  pass