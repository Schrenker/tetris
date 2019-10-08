class Tile:
    def __init__(self, upleft, upright, downleft, downright):
        self.upleft = upleft
        self.upright = upright
        self.downleft = downleft
        self.downright = downright



def create_tileview(height, width):
    tileview = []
    for i in range(height):
        tileview.append([])
        for j in range(width):
            tileview[i].append(
                Tile(
                    [2 * i + 1, 2 * j + 1],
                    [2 * i + 1, 2 * j + 2],
                    [2 * i + 2, 2 * j + 1],
                    [2 * i + 2, 2 * j + 2],
                )
            )
    return tileview
