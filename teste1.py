import unittest
from DESAFIO1 import sum_intervals

intervalos = [
    [1, 5],
    [10, 20],
    [1, 6],
    [16, 19],
    [5, 11]
]


def caso1():
    assert sum_intervals(intervalos)
    print("OK - 1")


if __name__ == "__main__":
    caso1()