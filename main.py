import inquirer

import helpers.color_text as color

from classes.File import File

from helpers.menu_helper import menu
from helpers.menu_helper import handle_choice
from helpers.file_maker import file_maker

from utils.clear_screen import clear_screen
from utils.print_banner import print_banner

def main():
  file_maker(File.FILE_COMMANDS.value)
  file_maker(File.FILE_ENDPOINTS.value)
  file_maker(File.FILE_ERRORS.value)
  file_maker(File.FILE_IDS.value)
  file_maker(File.FILE_KEYS.value)

  clear_screen()
  color.banner(print_banner())
  
  while True:
    user_respond = inquirer.prompt(menu)
    handle_choice(user_respond)

if __name__ == "__main__":
  main()
