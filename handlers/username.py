import inquirer
import helpers.color_text as color

from classes.File import File
from classes.Option import Option

from helpers.file_reader import file_reader
from helpers.file_writer import file_writer, overwrite_file
from utils.clear_screen import clear_screen

_FILE_USERNAME = File.FILE_USERNAMES.value

_user_menu = [
  inquirer.List("choice",
    message = "Choose your Username Activity",  
    choices=[
      Option.USERNAME_1.value,
      Option.USERNAME_2.value,
      Option.USERNAME_3.value,
      Option.USERNAME_4.value,
      Option.EXIT.value
    ],
    carousel=True
  )
]

def _count_usernames():
  content = file_reader(_FILE_USERNAME)