import helpers.color_text as color

def read(file: str):
  try:
    with open(file) as f:
      payloads = f.readlines()
  except Exception as err:
    message = color.warning(err)
    print(message)
  return payloads