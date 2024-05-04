import inquirer
import helpers.color_text as color

from classes.Option import Option

from helpers.file_reader import file_reader
from utils.clear_screen import clear_screen

dictionary_menu = [
  inquirer.List("choice",
    message = "Choose your Endpoint Activity",
    choices=[
      Option.DICTIONARY_1.value,
      Option.DICTIONARY_2.value,
      Option.DICTIONARY_3.value,
      Option.DICTIONARY_4.value,
      Option.EXIT.value,
    ],
    carousel=True
  ),
]

def count_dictionary():
  content = file_reader("dictionary/passwords.txt")
  message = f"There are total of {len(content)} words available in passwords.\n"
  color.light_green(message)
  
def search_dictionary():
  pass

def add_dictionary():
  pass

def delete_dictionary():
  pass

def handle_dictionary(banner):
  clear_screen()
  color.banner(banner)
  user_respond = inquirer.prompt(dictionary_menu)
  choice = user_respond["choice"]

  if choice == Option.DICTIONARY_1.value:
    count_dictionary()

  elif choice == Option.DICTIONARY_2.value:
    search_dictionary()

  elif choice == Option.DICTIONARY_3.value:
    add_dictionary()

  elif choice == Option.DICTIONARY_4.value:
    delete_dictionary()

  elif choice == Option.EXIT.value:
    clear_screen()