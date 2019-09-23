import consts as const
import curses
from view.game_window import GameWindow
from view.menu_window import MenuWindow


class View:
    def __init__(self):
        self.menu_window = MenuWindow()
        self.game_window = GameWindow()
        self.block_window = curses.newwin(10, 8, 1, const.WIDTH * 2 + 4)
        self.score_window = curses.newwin(8, 8, 11, const.WIDTH * 2 + 4)

    def render_frame(self, figure, game_state):
        self.clear()
        self.render_box()
        self.game_window.render_figure(figure)
        self.game_window.render_state(game_state)

    def clear(self):
        self.game_window.window.clear()
        self.block_window.clear()
        self.score_window.clear()

    def render_box(self):
        self.game_window.window.box()
        self.block_window.box()
        self.score_window.box()

    def refresh(self):
        self.game_window.window.refresh()
        self.block_window.refresh()
        self.score_window.refresh()
