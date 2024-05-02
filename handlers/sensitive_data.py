import inquirer
import helpers.color_text as color

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
    content = file_reader("dictionary/sensitive_keys.txt")
    message = f"There are total of {len(content)} words available in sensitive keys.\n"
    color.light_green(message)

def search_sensitive_data():
  pass