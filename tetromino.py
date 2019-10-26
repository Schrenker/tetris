# functions that are basically shapes library, with predefined colors,
# coordinates that only require being moved to the middle and rotation check
# STABLE ROTATION

def create_L():
    L = [[1, 1], [1, 1], [0, 1], [2, 1], [2, 2]]
    color = 1
    rotateable = True
    return L, color, rotateable


def create_J():
    J = [[1, 1], [1, 1], [0, 1], [2, 1], [2, 0]]
    color = 2
    rotateable = True
    return J, color, rotateable


def create_T():
    T = [[1, 1], [1, 1], [0, 1], [2, 1], [1, 2]]
    color = 3
    rotateable = True
    return T, color, rotateable


# PIVOT SWAPPING ROTATION


def create_I():
    I = [[2, 1], [3, 1], [1, 1], [0, 1]]
    color = 4
    rotateable = True
    return I, color, rotateable


def create_S():
    S = [[1, 1], [0, 1], [0, 2], [1, 0]]
    color = 5
    rotateable = True
    return S, color, rotateable


def create_Z():
    Z = [[1, 1], [0, 1], [1, 2], [0, 0]]
    color = 6
    rotateable = True
    return Z, color, rotateable


# NO ROTATION


def create_O():
    O = [[1, 1], [0, 1], [1, 2], [0, 2]]
    color = 7
    rotateable = False
    return O, color, rotateable

# this dictionary is being exported, it's basically all shapes packed into one
# variable. Keys are numbers from 0 to 6, which trivializes randomization
# process
tetrominos = {
    0: create_L,
    1: create_J,
    2: create_I,
    3: create_O,
    4: create_S,
    5: create_Z,
    6: create_T,
}
