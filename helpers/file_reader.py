import helpers.color_text as color

from helpers.file_maker import file_maker

def file_reader(file : str):
  try:
    file_maker(file)
    with open(file) as f:
      content = f.readlines()
  except Exception as err:
    message = color.warning(f"An error occurred: {err}")
    print(message)
  return content