# This class is used for graphical representation of blocks. Right now it shows
# 1x1 tile as 2x2 tiles, but can be easily modified to show any
# dimension of tiles.
class Tile:
    def __init__(self, upleft, upright, downleft, downright):
        self.upleft = upleft
        self.upright = upright
        self.downleft = downleft
        self.downright = downright



def create_tileview(height, width, offsety, offsetx):
    tileview = []
    for i in range(height):
        tileview.append([])
        for j in range(width):
            tileview[i].append(
                Tile(
                    [2 * i + 1 + offsety, 2 * j + 1 + offsetx],
                    [2 * i + 1 + offsety, 2 * j + 2 + offsetx],
                    [2 * i + 2 + offsety, 2 * j + 1 + offsetx],
                    [2 * i + 2 + offsety, 2 * j + 2 + offsetx],
                )
            )
    return tileview
