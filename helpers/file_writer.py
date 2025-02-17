import os

import helpers.color_text as color

def file_writer(file_name : str, text):
  try:
    create_files_folder()
    folder_path = ""
    
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'a') as file:
      file.write(str(text) + '\n')

    message = color.light_green("text has been saved.")
    print(message)

  except Exception as err:
    message = color.warning(f"An error occurred: {err}")
    print(message)

def overwrite_file(file_name: str, new_content: list):
  try:
    create_files_folder()
    folder_path = ""

    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as file:
      file.writelines(f"{line}\n" for line in new_content)

  except Exception as err:
    message = color.warning(f"An error occurred: {err}")
    print(message)

def create_files_folder():
  folder_path = "files"
  if not os.path.exists(folder_path):
    os.makedirs(folder_path)