import consts as const
import json


class GameState:
    def __init__(self):
        self.has_died = False
        self.name = ""
        self.score = 0
        self.highest_score = 0
        self.load_score()

    def generate_play_field(self):
        self.area = []
        for i in range(const.HEIGHT):
            self.area.append([])
            for j in range(const.WIDTH):
                self.area[i].append([" ", 0])

    def add_figure_to_state(self, figure):
        for i in range(len(figure.shape)):
            self.area[figure.shape[i][0]][figure.shape[i][1]] = [
                "X",
                figure.color,
            ]

    def check_full_rows(self):
        combo = 1
        i = len(self.area) - 1
        while i >= 0:
            if all(elem[0] == "X" for elem in self.area[i]):
                self.score += const.SCORE_INCREASE * combo
                combo += 1
                for j in range(i, 0, -1):
                    self.area[j] = self.area[j - 1].copy()
            else:
                i -= 1

    def load_score(self):
        with open("./.highscores.json", "r") as f:
            self.score_table = json.load(f)
            self.highest_score = self.score_table["0"][0]
            f.close()

    def save_score(self):
        with open("./.highscores.json", "w") as f:
            json.dump(self.score_table, f)
            f.close()

    def sort_score_table(self):
        for i in range(10):
            for j in range(i, 10):
                if self.score_table[str(i)] < self.score_table[str(j)]:
                    self.score_table[str(i)], self.score_table[str(j)] = (
                        self.score_table[str(j)],
                        self.score_table[str(i)],
                    )

    def check_final_score(self):
        # added without trying, fix
        if self.score > self.score_table["9"][0]:
            self.score_table["9"][0] = self.score
            self.score_table["9"][1] = self.name
            self.sort_score_table()
            self.save_score()
        self.has_died = True
