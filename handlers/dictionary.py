import inquirer

from classes.Option import Option

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

def add_dictionary():
  pass

def read_dictionary():
  pass

def update_dictionary():
  pass

def delete_dictionary():
  pass

def handle_dictionary():
  clear_screen()
  user_respond = inquirer.prompt(dictionary_menu)
  choice = user_respond["choice"]

  if choice == Option.DICTIONARY_1.value:
    add_dictionary()

  elif choice == Option.DICTIONARY_2.value:
    read_dictionary()