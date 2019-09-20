import consts as const


class GameState:
    def __init__(self):
        self.area = []
        for i in range(const.HEIGHT):
            self.area.append([])
            for j in range(const.WIDTH):
                self.area[i].append([" ", 0])
        self.score = 0

    def add_figure_to_state(self, figure):
        for i in range(len(figure.shape)):
            self.area[figure.shape[i][0]][figure.shape[i][1]] = [
                "X",
                figure.color,
            ]

    def check_full_rows(self):
        combo = 1
        for i in range(len(self.area) - 1, 0, -1):
            if all(elem[0] == "X" for elem in self.area[i]):
                self.score += const.SCORE_INCREASE * combo
                combo += 1
                for j in range(i, 0, -1):
                    self.area[j] = self.area[j - 1]
                    i = 0
