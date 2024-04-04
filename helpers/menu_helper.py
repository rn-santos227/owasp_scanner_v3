import inquirer
import sys

from enums.option import Option

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
      Option.OPTION_9.value,
      Option.EXIT.value,
    ],
    carousel=True
  ),
]

def handle_choice(respond):
  choice = respond["choice"]
  if choice == Option.OPTION_1.value:
    print("You selected: Add New Endpoint")

  elif choice == Option.OPTION_2.value:
    print("You selected: Manage Endpoints Collection")

  elif choice == Option.OPTION_3.value:
    print("You selected: Perform Full Scan")

  elif choice == Option.OPTION_4.value:
    print("You selected: Perform Quick Scan")

  elif choice == Option.OPTION_5.value:
    print("You selected: Perform Specific Scan")

  elif choice == Option.OPTION_6.value:
    print("You selected: Check Bruteforce Dictionary")

  elif choice == Option.OPTION_7.value:
    print("You selected: Check Sensitive Data Bank")

  elif choice == Option.OPTION_8.value:
    print("You selected: Adjust Program Rate Call")

  elif choice == Option.OPTION_9.value:
    print("You selected: Open Instruction Manual")

  elif choice == "Exit Program":
    print("Exiting Program...")
    sys.exit()