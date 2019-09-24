from view.game_window import GameWindow
from view.menu_window import MenuWindow
from view.block_window import BlockWindow
from view.score_window import ScoreWindow


class View:
    def __init__(self):
        self.menu_window = MenuWindow()
        self.game_window = GameWindow()
        self.block_window = BlockWindow()
        self.score_window = ScoreWindow()

    def render_frame(self, figure, game_state):
        self.erase()
        self.render_box()
        self.game_window.render_figure(figure)
        self.game_window.render_state(game_state)
        self.score_window.render_score(game_state.score)

    def clear(self):
        self.game_window.window.clear()
        self.block_window.window.clear()
        self.score_window.window.clear()

    def erase(self):
        self.game_window.window.erase()
        self.menu_window.window.erase()
        self.score_window.window.erase()
        self.block_window.window.erase()

    def render_box(self):
        self.game_window.window.box()
        self.block_window.window.box()
        self.score_window.window.box()

    def refresh(self):
        self.game_window.window.refresh()
        self.block_window.window.refresh()
        self.score_window.window.refresh()
