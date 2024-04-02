import inquirer

menu = [
  inquirer.List("choice",
    message = "Choose your Activity",
    choices = [
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
  ),
]

def select_menu(respond):
  pass