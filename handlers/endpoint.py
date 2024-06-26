import inquirer
import helpers.color_text as color

from classes.Option import Option

from helpers.file_reader import file_reader
from utils.clear_screen import clear_screen

endpoint_menu = [
  inquirer.List("choice",
    message = "Choose your Endpoint Activity",
    choices=[
      Option.ENDPOINT_1.value,
      Option.ENDPOINT_2.value,
      Option.ENDPOINT_3.value,
      Option.ENDPOINT_4.value,
      Option.EXIT.value,
    ],
    carousel=True
  ),
]

def create_endpoint():
  pass

def read_endpoint():
  pass

def update_endpoint():
  pass

def delete_endpoint():
  pass

def handle_endpoint(banner):
  clear_screen()
  color.banner(banner)
  user_respond = inquirer.prompt(endpoint_menu)
  choice = user_respond["choice"]

  if choice == Option.ENDPOINT_1.value:
    create_endpoint()

  elif choice == Option.ENDPOINT_2.value:
    read_endpoint()

  elif choice == Option.ENDPOINT_3.value:
    update_endpoint()

  elif choice == Option.ENDPOINT_4.value:
    delete_endpoint()

  elif choice == Option.EXIT.value:
    clear_screen()