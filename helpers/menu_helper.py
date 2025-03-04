import inquirer
import sys

from classes.Option import Option

from handlers.dictionary import handle_dictionary
from handlers.endpoint import handle_endpoint
from handlers.sensitive_data import handle_sensitive_data
from handlers.settings import handle_config
from handlers.token import handle_token

menu = [
  inquirer.List("choice",
    message = "Choose your Activity",
    choices=[
      Option.OPTION_01.value,
      Option.OPTION_02.value,
      Option.OPTION_03.value,
      Option.OPTION_04.value,
      Option.OPTION_05.value,
      Option.OPTION_06.value,
      Option.OPTION_07.value,
      Option.OPTION_08.value,
      Option.OPTION_09.value,
      Option.OPTION_10.value,
      Option.EXIT.value
    ],
    carousel=True
  ),
]

def handle_choice(respond):
  choice = respond["choice"]
  if choice == Option.OPTION_01.value:
    banner = f"You selected: {Option.OPTION_01.value}"
    handle_endpoint(banner)

  elif choice == Option.OPTION_02.value:
    print(f"You selected: {Option.OPTION_02.value}")

  elif choice == Option.OPTION_03.value:
    print(f"You selected: {Option.OPTION_03.value}")

  elif choice == Option.OPTION_04.value:
    print(f"You selected: {Option.OPTION_04.value}")

  elif choice == Option.OPTION_05.value:
    banner = f"You selected: {Option.OPTION_05.value}"
    handle_dictionary(banner)

  elif choice == Option.OPTION_06.value:
    banner = f"You selected: {Option.OPTION_06.value}"
    handle_sensitive_data(banner)
    
  elif choice == Option.OPTION_07.value:
    banner = f"You selected: {Option.OPTION_07.value}"
    handle_token(banner)

  elif choice == Option.OPTION_08.value:
    banner = f"You selected: {Option.OPTION_08.value}"

  elif choice == Option.OPTION_09.value:
    banner = f"You selected: {Option.OPTION_09.value}"
    handle_config(banner)

  elif choice == Option.OPTION_9.value:
    print(f"You selected: {Option.OPTION_9.value}")

  elif choice == Option.EXIT.value:
    print("Exiting Program...")
    sys.exit()