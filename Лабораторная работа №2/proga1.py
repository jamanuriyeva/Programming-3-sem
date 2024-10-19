import logging
#настройка логирования
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def log_decorator(fn):
    def wrapper(num1, num2, operator):
        logger.info(f'Введенные операнды и операция: {num1}, {num2}, {operator}')
        result = fn(num1, num2, operator)
        logger.info("Result: %s.", result)
        return result

    return wrapper


@log_decorator
def calculate(num1, num2, operator):
    """
    Функция совершающая действия с числами в зависимости от выбранного действия
    :param num1: float первое чилсло
    :param num2: float второе число
    :param operator: str действие
    :return: результат
    """

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/' and num2 != 0:
        return num1 / num2
    elif operator == '/' and num2 == 0:
        return "You can't divide by zero!"

# def main():
#     """
#     Функция считывает первое число, второе число и действие, которое необходимо совершить с этими числоми
#
#     """
#     num1 = float(input("Введите первое число: "))
#     num2 = float(input("Введите второе число: "))
#     operator = input("Выберите действие ('+', '/', '*'): ")
#     result = calculate(num1, num2, operator)
#     print(result)
#
# main()

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






