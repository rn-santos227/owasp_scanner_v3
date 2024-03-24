import helpers.color_text as color

ignore_status_code = 0

def handle_status_code(status_code):
  global ignore_status_code
  if (status_code // 100 == 4 or status_code // 100 == 5) and ignore_status_code == 0:
    color.warning(f"Response status code is {status_code}")
    while True:
      answer = input("Continue? y/n: ")

      if answer.lower() not in ['y','n']:
        color.warning("Invalid Input.")
        continue

      if answer.lower() == 'y':
        ignore_status_code = 1 
      else:
        print("SYSTEM CLOSING. BYE.")
        exit(0)