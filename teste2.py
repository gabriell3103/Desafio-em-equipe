import unittest
from DESAFIO2 import move_zeros


def caso_1():
    assert move_zeros([0, 5, 31, 0, 9, 0, 0, 10, 50]) == [
        5, 31, 9, 10, 50, 0, 0, 0, 0]
    print("OK - 2")


if __name__ == "__main__":
    caso_1()