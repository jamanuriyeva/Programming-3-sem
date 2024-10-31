import logging
from convert_precision import convert_precision
import math
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
    elif operator == 'medium':
        n = len(args)
        medium = sum(args) / n
        return round(medium, convert_precision(tolerance))
    elif operator == 'varians':
        n = len(args)
        mean = sum(args) / n
        deviations = [(num - mean) ** 2 for num in args]
        variance = sum(deviations) / (n - 1)
        return round(variance, convert_precision(tolerance))
    elif operator == 'std_deviation':
        n = len(args)
        mean = sum(args) / n
        deviations = [(num - mean) ** 2 for num in args]
        variance = sum(deviations) / (n - 1)
        std_deviation = math.sqrt(variance)
        return round(std_deviation, convert_precision(tolerance))
    elif operator == 'median':
        sorted_numbers = sorted(args)
        length = len(sorted_numbers)

        if length % 2 == 0:
            middle_1 = sorted_numbers[length // 2 - 1]
            middle_2 = sorted_numbers[length // 2]
            median = (middle_1 + middle_2) / 2
        else:
            median = sorted_numbers[(length - 1) // 2]

        return round(median, convert_precision(tolerance))
    elif operator == 'IQR':
        sorted_numbers = sorted(args)
        n = len(sorted_numbers)
        q1_index = int((n + 1) * 0.25) - 1
        q3_index = int((n + 1) * 0.75) - 1
        q1 = sorted_numbers[q1_index]
        q3 = sorted_numbers[q3_index]
        iqr_value = q3 - q1
        return round(iqr_value, convert_precision(tolerance))


def main():
    """
    Функция считывает действие и числа, которые необходимо обработать.
    """
    operator = input("Выберите действие ('+', '-', '/', '*', 'medium', 'variance', 'std_deviation', 'median', 'IQR): ")
    numbers = list(map(float, input("Введите числа через пробел: ").split()))

    # Вызов функции расчета
    result = calculate(*numbers, operator=operator)  # Передаем все числа и оператор
    print(f"Результат: {result}")

main()
