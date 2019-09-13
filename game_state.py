import consts as const


class GameField:
    def __init__(self):
        self.area = []
        for i in range(const.HEIGHT):
            self.area.append([])
            for j in range(const.WIDTH):
                self.area[i].append(" ")

    def add_figure_to_state(self, figure):
        for i in range(len(figure.shape)):
            self.area[figure.shape[i][0]][figure.shape[i][1]] = "X"

    def render_state(self, window):
        for i in range(len(self.area)):
            for j in range(len(self.area[0])):
                if self.area[i][j] == "X":
                    window.addch(i, j, "X")
