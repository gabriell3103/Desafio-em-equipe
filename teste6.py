import unittest
from desafio_6 import WordSquare


def caso_1():
    assert WordSquare("SATORAREPOTENETOPERAROTAS") == True
    print("OK - 1")


def caso_2():
    assert WordSquare("NOTSQUARE") == False
    print("OK - 2")


if __name__ == '__main__':
    caso_1()
    caso_2()