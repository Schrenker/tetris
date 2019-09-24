import curses
import consts as const


class BlockWindow:
    def __init__(self):
        self.window = curses.newwin(10, 8, 1, const.WIDTH * 2 + 4)
