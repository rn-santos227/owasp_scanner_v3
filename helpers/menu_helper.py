import inquirer
import sys

from enums.option import Option

menu = [
  inquirer.List("choice",
    message = "Choose your Activity",
    choices=[
      "Add New Endpoint",
      "Manage Endpoints Collection",
      "Perform Full Scan",
      "Perform Quick Scan",
      "Perform Specific Scan",
      "Check Bruteforce Dictionary",
      "Check Sensitive Data Bank",
      "Adjust Program Rate Call",
      "Open Instruction Manual",
      "Exit Program"
    ],
    carousel=True
  ),
]

def handle_choice(respond):
  choice = respond["choice"]
  if choice == "Add New Endpoint":
    print("You selected: Add New Endpoint")

  elif choice == "Exit Program":
    print("Exiting Program...")
    sys.exit()