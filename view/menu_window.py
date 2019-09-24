import curses
import consts as const


class MenuWindow:
    def __init__(self):
        self.window = curses.newwin(const.HEIGHT * 3, const.WIDTH * 5, 0, 0)


    def instructions(self):
        self.window.addstr(5, 5, "Press Q to exit")
        self.window.addstr(6, 5, "Press any other key to start")
