import unittest
from DESAFIO4 import balanced_parens


def caso_1():
    assert balanced_parens(0) == ['']
    print("OK - 1")


def caso_2():
    assert balanced_parens(1) == ['()']
    print("OK - 2")


def caso_3():
    assert balanced_parens(
        3) == ['()()()', '()(())', '(())()', '(()())', '((()))']
    print("OK - 3")


if __name__ == "__main__":
    caso_1()
    caso_2()
    caso_3()