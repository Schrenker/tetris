class Figure:
    def __init__(self):
        pass

    def create_new_shape(self):
        self.shapes = [[1, 16], [0, 16], [2, 16], [1, 17]]

    def move_down(self):
        for coord in self.shapes:
            coord[0] += 1

    def move_left(self):
        for coord in self.shapes:
            coord[1] -= 1

    def move_right(self):
        for coord in self.shapes:
            coord[1] += 1

    def render(self, window):
        for coord in self.shapes:
            window.addch(coord[0], coord[1], "X")

    def rotate(self, window):
        for i in range(1, len(self.shapes)):
            x, y = self.shapes[i][1], self.shapes[i][0]
            self.shapes[i] = [(x - self.shapes[0][1]) + self.shapes[0][0], (y - self.shapes[0][0]) * -1 + self.shapes[0][1]]
            self.render(window)
