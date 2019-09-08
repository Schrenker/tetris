import curses
import consts as const


def main(stdscr):

    #curses init
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    stdscr.nodelay(True)

    gameWindow = curses.newwin(const.HEIGHT, const.WIDTH, 2, 2)
    gameWindow.keypad(1)
    gameWindow.timeout(const.TIMEOUT)


if __name__ == "__main__":
    curses.wrapper(main)
