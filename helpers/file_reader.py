import os

import helpers.color_text as color

def file_reader(file : str):
  try:
    with open(file) as f:
      content = f.readlines()
  except Exception as err:
    message = color.warning(f"An error occurred: {err}")
    print(message)
  return content