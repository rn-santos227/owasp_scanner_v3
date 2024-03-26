import curses

def main(stdscr):
  curses.curs_set(0)
  stdscr.clear()
  stdscr.refresh()

  options = ["Option 1", "Option 2", "Option 3", "Exit"]
  selected_option = 0
  pass