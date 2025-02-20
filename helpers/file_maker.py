import os
import helpers.color_text as color

def file_maker(file_path):
  try:
    folder_path = os.path.dirname(file_path)

    if folder_path and not os.path.exists(folder_path):
      os.makedirs(folder_path)
      color.light_green(f"✓ Folder '{folder_path}' created.")

    if not os.path.exists(file_path):
      with open(file_path, 'w') as file:
        pass

  except Exception as err:
    color.warning(f"An error occurred: {err}")