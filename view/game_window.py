import curses
import consts as const
from view.tile import Tile

class GameWindow:
    def __init__(self):
        self.window = curses.newwin(
            const.HEIGHT * 2 + 2, const.WIDTH * 2 + 2, 1, 1
        )
        self.window.keypad(1)
        self.window.timeout(const.TIMEOUT)
        self.game_view = self.create_tileview()
        self.prev_figure_coords = [[0, 0]]

    def create_tileview(self):
        view = []
        for i in range(const.HEIGHT):
            view.append([])
            for j in range(const.WIDTH):
                view[i].append(
                    Tile(
                        [2 * i + 1, 2 * j + 1],
                        [2 * i + 1, 2 * j + 2],
                        [2 * i + 2, 2 * j + 1],
                        [2 * i + 2, 2 * j + 2],
                    )
                )
        return view

    def render_figure(self, figure):
        for coord in figure.shape:
            self.window.addstr(
                self.game_view[coord[0]][coord[1]].upleft[0],
                self.game_view[coord[0]][coord[1]].upleft[1],
                "X",
                curses.color_pair(figure.color),
            )
            self.window.addstr(
                self.game_view[coord[0]][coord[1]].upright[0],
                self.game_view[coord[0]][coord[1]].upright[1],
                "X",
                curses.color_pair(figure.color),
            )
            self.window.addstr(
                self.game_view[coord[0]][coord[1]].downleft[0],
                self.game_view[coord[0]][coord[1]].downleft[1],
                "X",
                curses.color_pair(figure.color),
            )
            self.window.addstr(
                self.game_view[coord[0]][coord[1]].downright[0],
                self.game_view[coord[0]][coord[1]].downright[1],
                "X",
                curses.color_pair(figure.color),
            )

    def render_state(self, game_state):
        for i in range(const.HEIGHT - 1, 0, -1):
            is_row_empty = True
            for j in range(const.WIDTH):
                if game_state.area[i][j][0] == "X":
                    is_row_empty = False
                    self.window.addstr(
                        self.game_view[i][j].upleft[0],
                        self.game_view[i][j].upleft[1],
                        "X",
                        curses.color_pair(game_state.area[i][j][1]),
                    )
                    self.window.addstr(
                        self.game_view[i][j].upright[0],
                        self.game_view[i][j].upright[1],
                        "X",
                        curses.color_pair(game_state.area[i][j][1]),
                    )
                    self.window.addstr(
                        self.game_view[i][j].downleft[0],
                        self.game_view[i][j].downleft[1],
                        "X",
                        curses.color_pair(game_state.area[i][j][1]),
                    )
                    self.window.addstr(
                        self.game_view[i][j].downright[0],
                        self.game_view[i][j].downright[1],
                        "X",
                        curses.color_pair(game_state.area[i][j][1]),
                    )
            if is_row_empty:
                return

