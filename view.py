import consts as const
import curses


class View:
    def __init__(self):
        self.game_window = curses.newwin(
            const.HEIGHT * 2 + 2, const.WIDTH * 2 + 2, 1, 1
        )
        self.game_window.keypad(1)
        self.game_window.timeout(const.TIMEOUT)
        self.block_window = curses.newwin(10, 8, 1, const.WIDTH * 2 + 4)
        self.score_window = curses.newwin(8, 8, 11, const.WIDTH * 2 + 4)
        self.view = self.create_tileview()
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

    def render(self):
        for i in range(const.HEIGHT):
            for j in range(const.WIDTH):
                if self.view[i][j].active:
                    self.game_window.addch(
                        self.view[i][j].upleft[0],
                        self.view[i][j].upleft[1],
                        "X",
                    )
                    self.game_window.addch(
                        self.view[i][j].upright[0],
                        self.view[i][j].upright[1],
                        "X",
                    )
                    self.game_window.addch(
                        self.view[i][j].downleft[0],
                        self.view[i][j].downleft[1],
                        "X",
                    )
                    self.game_window.addch(
                        self.view[i][j].downright[0],
                        self.view[i][j].downright[1],
                        "X",
                    )

    def update_figure_position(self, figure):
        for coord in self.prev_figure_coords:
            self.view[coord[0]][coord[1]].active = False
        for coord in figure.shape:
            self.view[coord[0]][coord[1]].active = True
        self.prev_figure_coords = figure.shape[:]

    def update_game_state(self, game_state):
        for i in range(const.HEIGHT):
            for j in range(const.WIDTH):
                if game_state.area[i][j] == "X":
                    self.view[i][j].active = True
                else:
                    self.view[i][j].active = False

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


class Tile:
    def __init__(self, upleft, upright, downleft, downright):
        self.active = False
        self.upleft = upleft
        self.upright = upright
        self.downleft = downleft
        self.downright = downright
