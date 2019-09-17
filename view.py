import consts as const
import curses


class View:
    def __init__(self):
        self.game_window = curses.newwin(
            const.HEIGHT * 2 + 2, const.WIDTH * 2 + 2, 1, 1
        )
        self.game_window.keypad(1)
        self.game_window.timeout(const.TIMEOUT)
        self.block_window = curses.newwin(
            10, 8, 1, const.WIDTH * 2 + 4
        )
        self.score_window = curses.newwin(
            8, 8, 10, const.WIDTH * 2 + 4
        )

    def clear(self):
        self.game_window.clear()
        self.block_window.clear()
        self.score_window.clear()

    def render_box(self):
        self.game_window.box()
        self.block_window.box()
        self.score_window.box()

    def refresh(self):
        self.game_window.refresh()
        self.block_window.refresh()
        self.score_window.refresh()
