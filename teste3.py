import unittest
from DESAFIO3 import girar_matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def caso_clockwise():
    assert girar_matriz(matriz, 'clockwise') == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    print('OK - clockwise')


def caso_counter_clockwise():
    assert girar_matriz(
        matriz, 'counter-clockwise') == [
        [3, 6, 9],
        [2, 5, 8],
        [1, 4, 7]
    ]
    print('OK - counter-clockwise')


if __name__ == "__main__":
    caso_clockwise()
    caso_counter_clockwise()