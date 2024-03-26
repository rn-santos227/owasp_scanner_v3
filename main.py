import curses

def main(stdscr):
  curses.curs_set(0)
  stdscr.clear()
  stdscr.refresh()

  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN) 

  options = ["Option 1", "Option 2", "Option 3", "Exit Program"]
  selected_option = 0

  while True:
    stdscr.clear()
    
    for index, option in enumerate(options):
      if index == selected_option:
        stdscr.addstr(index, 0, "> ", curses.color_pair(1) | curses.A_REVERSE) 
        stdscr.addstr(option + "\n", curses.color_pair(1)) 
      else:
        stdscr.addstr(index, 0, "  " + option + "\n") 
    
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
