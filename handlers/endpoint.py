import inquirer
import sys

from enums.option import Option

endpoint_menu = [
  inquirer.List("choice",
    message = "Choose your Endpoint Activity",
    choices=[
      Option.ENDPOINT_1.value,
      Option.ENDPOINT_2.value,
      Option.ENDPOINT_3.value,
      Option.EXIT.value,
    ],
    carousel=True
  ),
]

def create_endpoint():
  pass

def read_endpoint():
  pass

def update_endpoint():
  pass

def delete_endpoint():
  pass

def handle_endpoint():
  pass