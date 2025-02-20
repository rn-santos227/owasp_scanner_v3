import os
import helpers.color_text as color

def file_maker(file_path):
  try:
    folder_path = os.path.dirname(file_path)

  except Exception as err:
    color.warning(f"An error occurred: {err}")