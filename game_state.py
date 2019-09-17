import consts as const


class GameState:
    def __init__(self):
        self.area = []
        for i in range(const.HEIGHT):
            self.area.append([])
            for j in range(const.WIDTH):
                self.area[i].append(" ")

    def add_figure_to_state(self, figure):
        for i in range(len(figure.shape)):
            self.area[figure.shape[i][0]][figure.shape[i][1]] = "X"

    def check_full_rows(self, score):
        combo = 1
        for i in range(len(self.area) - 1, 0, -1):
            if all(elem == 'X' for elem in self.area[i]):
                score += const.SCORE_INCREASE * combo
                combo += 1
                for j in range(i, 0, -1):
                    self.area[j] = self.area[j - 1]
                    i = 0
        return score

    def render_state(self, window):
        for i in range(len(self.area)):
            for j in range(len(self.area[0])):
                if self.area[i][j] == "X":
                    window.addch(i + 1, j + 1, "X")
