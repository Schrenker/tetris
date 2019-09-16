def create_L():
    L = [[1, 5], [0, 5], [2, 5], [2, 6]]
    color = 0
    return L, color

def create_J():
    J = [[1, 5], [0, 5], [2, 5], [2, 4]]
    color = 1
    return J, color


def create_I():
    I = [[1, 5], [0, 5], [2, 5], [3, 5]]
    color = 2
    return I, color

def create_O():
    O = [[1, 5], [0, 5], [1, 6], [0, 6]]
    color = 3
    return O, color


def create_S():
    S = [[1, 5], [0, 5], [0, 6], [1, 4]]
    color = 4
    return S, color


def create_Z():
    Z = [[1, 5], [0, 5], [1, 6], [0, 4]]
    color = 5
    return Z, color


def create_T():
    T = [[1, 5], [0, 5], [2, 5], [1, 6]]
    color = 6
    return T, color

tetrominos = {
    0: create_L,
    1: create_J,
    2: create_I,
    3: create_O,
    4: create_S,
    5: create_Z,
    6: create_T
}
