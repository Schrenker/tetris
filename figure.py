class Figure:
    def __init__(self):
        pass

    def create_new_shape(self):
        self.shape = [[1, 5], [0, 5], [2, 5], [1, 6]]

    def move_down(self):
        for coord in self.shape:
            coord[0] += 1

    def move_left(self):
        for coord in self.shape:
            coord[1] -= 1

    def move_right(self):
        for coord in self.shape:
            coord[1] += 1

    def render(self, window):
        for coord in self.shape:
            window.addch(coord[0], coord[1], "X")

    # first coord in shapes is ALWAYS the pivot
    def rotate(self, window):
        for i in range(1, len(self.shape)):
            x, y = self.shape[i][1], self.shape[i][0]
            self.shape[i] = [
                (x - self.shape[0][1]) + self.shape[0][0],
                (y - self.shape[0][0]) * -1 + self.shape[0][1],
            ]
            self.render(window)
