import os
import sys
import msvcrt

import classes.Cursor as Cursor

def print_options(options, selected_option):
  os.system("cls" if os.name == "nt" else "clear")
  for i, option in enumerate(options):
    if i == selected_option:
      print(f"\033[7m{i + 1}. {option}\033[0m")
    
    else:
      print(f"{i + 1}. {option}")

def test():
  options = ["Option 1", "Option 2", "Option 3", "Exit"]
  selected_option = 0

  print_options(options, selected_option)
  while True:
    char = sys.stdin.read(1)

    if char == "\x1b":
      char2 = sys.stdin.read(1)
      char3 = sys.stdin.read(1)
      if char2 == '[':
        if char3 == 'A':
          selected_option = (selected_option - 1) % len(options)
        elif char3 == 'B':
          selected_option = (selected_option + 1) % len(options)
        print_options(options, selected_option)
    
    elif char == "\r":
      if selected_option == len(options) - 1:
        break

def move_cursor(x, y):
  sys.stdout.write("\033[%d;%dH" % (y, x))
  sys.stdout.flush()

def getch():
  return msvcrt.getch().decode("utf-8")

def handle_arrow_key(key):
  if key == 'H':
    move_cursor(10, 5)
    print("up")

  elif key == 'P':
    move_cursor(10, 5)
    print("down")

  elif key == 'M':
    move_cursor(10, 5)
    print("right")

  elif key == 'K':
    move_cursor(10, 5)
    print("left")

def main():
  while True:
    key = getch()
    if key == "\x03":
      print("bye")
      break
    handle_arrow_key(key)

if __name__ == "__main__":
  main()