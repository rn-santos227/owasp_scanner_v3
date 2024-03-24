def file_reader(file : str):
  try:
    with open(file) as f:
      payloads = f.readlines()
  except Exception as err:
    print(f"An error occurred: {err}")
  return payloads