import inquirer
import sys

menu = [
  inquirer.List("choice",
    message = "Choose your Activity",
    choices = [
      (1, "Add New Endpoint"),
      (2, "Manage Endpoints Collection"),
      (3, "Perform Full Scan"),
      (4, "Perform Quick Scan"),
      (5, "Perform Specific Scan"),
      (6, "Check Bruteforce Dictionary"),
      (7, "Check Sensitive Data Bank"),
      (8, "Adjust Program Rate Call"),
      (9, "Open Instruction Manual"),
      (10, "Exit Program")
    ],
  ),
]

def handle_choice(respond):
  choice = respond['choice']
  if choice == 1:
    print("You selected: Add New Endpoint")

  elif choice == 10:
    print("Exiting Program...")
    sys.exit()