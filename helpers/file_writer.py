import os

def file_writer(file_name : str, text):
  try:
    folder_path = "files"
    if not os.path.exists(folder_path):
      os.makedirs(folder_path)

    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'a') as file:
      file.write(str(text) + '\n')

  except Exception as err:
    print(f"An error occurred: {err}")