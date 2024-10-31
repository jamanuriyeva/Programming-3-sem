import logging
from convert_precision import convert_precision

import logging
from operator import add, sub, mul, truediv
from functools import reduce
from math import prod

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_decorator(fn):
    def wrapper(*args, operator=None):
        logger.info(f'Введенные операнды и операция: {args}, {operator}')
        result = fn(*args, operator=operator)
        logger.info(f"Result: {result}")
        return result

    return wrapper


@log_decorator
def calculate(*args, operator=None, tolerance = 0.000001):
    """
    Выполняет арифметическую операцию над числами и округляет результат на основе заданной точности.

    :param operator: Оператор для выполнения ('+', '-', '*', '/')
    :param tolerance: Значение точности (по умолчанию 1e-6)
    :param args: Произвольное количество чисел для обработки
    :return: Округленный результат операции
    """
    if operator == '+':
        return round(sum(args), convert_precision(tolerance))
    elif operator == '-':
        return round(reduce(sub, args), convert_precision(tolerance))
    elif operator == '*':
        return round(prod(args), convert_precision(tolerance))
    elif operator == '/' and all(arg != 0 for arg in args):
        return round(reduce(truediv, args), convert_precision(tolerance))
    elif operator == '/' and any(arg == 0 for arg in args):
        return "You can't divide by zero!"


def main():
    """
    Функция считывает действие и числа, которые необходимо обработать.
    """
    operator = input("Выберите действие ('+', '-', '/', '*'): ")
    numbers = list(map(float, input("Введите числа через пробел: ").split()))

    # Вызов функции расчета
    result = calculate(*numbers, operator=operator)  # Передаем все числа и оператор
    print(f"Результат: {result}")

main()
