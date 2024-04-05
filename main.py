import inquirer

import helpers.color_text as color

from helpers.menu_helper import menu
from helpers.menu_helper import handle_choice
from utils.clear_screen import clear_screen
from utils.print_banner import print_banner

def main():
  clear_screen()
  color.banner(print_banner())
  while True:
    user_respond = inquirer.prompt(menu)
    handle_choice(user_respond)

if __name__ == "__main__":
  main()
