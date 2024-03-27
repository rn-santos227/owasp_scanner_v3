import curses

import helpers.color_text as colors

from utils.print_banner import print_banner


def main(stdscr):
  curses.curs_set(0)
  stdscr.clear()
  stdscr.refresh()

  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN) 

  options = [
    "Add API Collections", 
    "Perform Full Scan", 
    "Perform Individual Scan",
    "Perform Quick Scan",
    "Check Bruteforce Dictionaries", 
    "Check Sensitive Data Bank", 
    "Adjust Endpoint Call Rate",
    "Exit OWASP Scanner"
  ]
    
  selected_option = 0

  while True:
    stdscr.clear()
    stdscr.addstr(1, 3, colors.banner(print_banner()))
    for index, option in enumerate(options):
      if index == selected_option:
        stdscr.addstr(index + 9, 3, "> ", curses.color_pair(1) | curses.A_REVERSE) 
        stdscr.addstr(option + "\n", curses.color_pair(1)) 
      else:
        stdscr.addstr(index + 9, 3, "  " + option + "\n") 
    
    stdscr.refresh()
    key = stdscr.getch()

    if key == curses.KEY_UP:
      selected_option = (selected_option - 1) % len(options)
    elif key == curses.KEY_DOWN:
      selected_option = (selected_option + 1) % len(options)
    elif key == curses.KEY_ENTER or key in [10, 13]:
      if selected_option == len(options) - 1: 
        break
      else:
        print(f"You selected: {options[selected_option]}")
        stdscr.getch()

if __name__ == "__main__":
  curses.wrapper(main)
