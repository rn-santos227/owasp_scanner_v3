import inquirer

import helpers.color_text as color

from helpers.menu_helper import menu
from helpers.menu_helper import select_menu
from utils.print_banner import print_banner

def main():
  color.banner(print_banner())
  while True:
    user_respond = inquirer.prompt(menu)

if __name__ == "__main__":
  main()
