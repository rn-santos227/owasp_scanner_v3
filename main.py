import curses
import sys
import time

def main():
  window = curses.initscr()
  dims = window.getmaxyx()
  if not curses.has_colors():
    curses.endwin()
    print("No Colors")
    sys.exit(0)
  else:
    curses.start_color()
  curses.noecho()
  curses.cbreak()
  curses.curs_set(0)
  main_loop(window, dims)

def main_loop(window, dims):
  window.clear()
  window.addstr("Exiting Program...")
  window.refresh()
  time.sleep(1)
  curses.noecho()
  curses.cbreak()
  curses.curs_set(1)
  curses.endwin()

if __name__ == "__main__":
  main()