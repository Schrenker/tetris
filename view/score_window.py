import curses
import consts as const


# this basic class is used to handle window with current score
class ScoreWindow:
    def __init__(self):
        self.window = curses.newwin(10, 20, 13, const.WIDTH * 2 + 4)

    def render_score(self, score, highest_score):
        self.window.addstr(2, 2, f"Score: {score}")
        self.window.addstr(4, 2, "Highest score:")
        self.window.addstr(5, 3, str(highest_score))
        self.window.addstr(7, 2, "Press Q to quit")
