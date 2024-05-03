import inquirer
import helpers.color_text as color

from classes.Option import Option

from helpers.file_reader import file_reader
from utils.clear_screen import clear_screen

sensitive_data_menu = [
  inquirer.List("choice",
    message = "Choose your Endpoint Activity",
    choices=[
      Option.DATA_1.value,
      Option.DATA_2.value,
      Option.DATA_3.value,
      Option.DATA_4.value,
      Option.EXIT.value,
    ],
    carousel=True
  ),
]

def count_sensitive_data():
  content = file_reader("dictionary/sensitive_keys.txt")
  message = f"There are total of {len(content)} words available in sensitive keys.\n"
  color.light_green(message)

def search_sensitive_data():
  banner = "Search a Text in Sensitive Data"

def add_sensitive_data():
  pass

def delete_sensitve_data():
  pass

def handle_sensitive_data():
  clear_screen()
  user_respond = inquirer.prompt(sensitive_data_menu)
  choice = user_respond["choice"]

  if choice == Option.DATA_1.value:
    count_sensitive_data()

  elif choice == Option.EXIT.value:
    clear_screen()