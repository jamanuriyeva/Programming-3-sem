from proga1 import calculate

def test_calcul1():
    """
    Функция для тестирования сложения функции calculate

    """
    assert calculate (3, 4, "+") == 7.0
test_calcul1()


def test_calcul2():
    """
    Функция для тестирования вычитания функции calculate

    """
    assert calculate(5, 4, "-") == 1.0
test_calcul2()


def test_calcul3():
    """
    Функция для тестирования умножения функции calculate

    """
    assert calculate(3, 4, "*") == 12.0
test_calcul3()

def test_calcul4():
    """
    Функция для тестирования деления функции calculate

    """
    assert calculate(10, 2, "/") == 5.0
test_calcul4()

def test_calcul5():
    """
    Функция для тестирования деления на ноль функции calculate

    """
    assert calculate(3, 0, "/") == "You can't divide by zero!"
test_calcul5()
