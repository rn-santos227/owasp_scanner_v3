import os

def file_writer(file : str):
  try:
    folder_path = "files"
    if not os.path.exists(folder_path):
      os.makedirs(folder_path)
      
  except Exception as err:
    print(f"An error occurred: {err}")