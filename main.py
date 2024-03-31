import inquirer

import helpers.color_text as color
from utils.print_banner import print_banner

def main():
  color.banner(print_banner())
  user_respond = inquirer.prompt(questions)

if __name__ == "__main__":
  main()
