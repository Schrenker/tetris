import curses
import consts as const


class ScoreWindow:
    def __init__(self):
        self.window = curses.newwin(10, 20, 11, const.WIDTH * 2 + 4)

    def render_score(self, score):
        self.window.addstr(2, 2, f"Score: {score}")
        self.window.addstr(4, 2, f"Highest score: {0}")
        self.window.addstr(7, 2, "Press Q to quit")
