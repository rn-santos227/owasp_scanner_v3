import inquirer
import sys

from classes.Option import Option

from handlers.dictionary import handle_dictionary
from handlers.endpoint import handle_endpoint
from handlers.sensitive_data import handle_sensitive_data
from handlers.settings import handle_config

menu = [
  inquirer.List("choice",
    message = "Choose your Activity",
    choices=[
      Option.OPTION_1.value,
      Option.OPTION_2.value,
      Option.OPTION_3.value,
      Option.OPTION_4.value,
      Option.OPTION_5.value,
      Option.OPTION_6.value,
      Option.OPTION_7.value,
      Option.OPTION_8.value,
      Option.EXIT.value,
    ],
    carousel=True
  ),
]

def handle_choice(respond):
  choice = respond["choice"]
  if choice == Option.OPTION_1.value:
    banner = f"You selected: {Option.OPTION_1.value}"
    handle_endpoint(banner)

  elif choice == Option.OPTION_2.value:
    print(f"You selected: {Option.OPTION_2.value}")

  elif choice == Option.OPTION_3.value:
    print(f"You selected: {Option.OPTION_3.value}")

  elif choice == Option.OPTION_4.value:
    print(f"You selected: {Option.OPTION_4.value}")

  elif choice == Option.OPTION_5.value:
    banner = f"You selected: {Option.OPTION_5.value}"
    handle_dictionary(banner)

  elif choice == Option.OPTION_6.value:
    banner = f"You selected: {Option.OPTION_6.value}"
    handle_sensitive_data(banner)
    
  elif choice == Option.OPTION_7.value:
    banner = f"You selected: {Option.OPTION_7.value}"
    handle_config(banner)

  elif choice == Option.OPTION_8.value:
    print(f"You selected: {Option.OPTION_8.value}")

  elif choice == Option.EXIT.value:
    print("Exiting Program...")
    sys.exit()