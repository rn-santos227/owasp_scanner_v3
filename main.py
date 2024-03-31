import inquirer
import re

import helpers.color_text as color
from utils.print_banner import print_banner

questions = [
  inquirer.List("choice",
    message="Choose your Activity",
    choices=[
      "Add an Endpoint", 
      "Manage Endpoints Collection", 
      "Perform Full Scan"
      "Perform Quick Scan", 
      "Perform Specific Scan", 
      "Exit Program"
    ],
  ),
]

def main():
  color.banner(print_banner())
  user_respond = inquirer.prompt(questions)

if __name__ == "__main__":
  main()
