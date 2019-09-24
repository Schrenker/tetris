import curses
import consts as const


class ScoreWindow:
    def __init__(self):
        self.window = curses.newwin(8, 8, 11, const.WIDTH * 2 + 4)
