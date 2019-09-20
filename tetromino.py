# STABLE ROTATION


def create_L():
    L = [[1, 5], [1, 5], [0, 5], [2, 5], [2, 6]]
    color = 1
    rotateable = True
    return L, color, rotateable


def create_J():
    J = [[1, 5], [1, 5], [0, 5], [2, 5], [2, 4]]
    color = 2
    rotateable = True
    return J, color, rotateable


def create_T():
    T = [[1, 5], [1, 5], [0, 5], [2, 5], [1, 6]]
    color = 3
    rotateable = True
    return T, color, rotateable


# PIVOT SWAPPING ROTATION


def create_I():
    I = [[2, 5], [3, 5], [1, 5], [4, 5]]
    color = 4
    rotateable = True
    return I, color, rotateable


def create_S():
    S = [[1, 5], [0, 5], [0, 6], [1, 4]]
    color = 5
    rotateable = True
    return S, color, rotateable


def create_Z():
    Z = [[1, 5], [0, 5], [1, 6], [0, 4]]
    color = 6
    rotateable = True
    return Z, color, rotateable


# NO ROTATION


def create_O():
    O = [[1, 5], [0, 5], [1, 6], [0, 6]]
    color = 7
    rotateable = False
    return O, color, rotateable


tetrominos = {
    0: create_L,
    1: create_J,
    2: create_I,
    3: create_O,
    4: create_S,
    5: create_Z,
    6: create_T,
}
