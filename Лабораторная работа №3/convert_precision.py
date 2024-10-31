import math
def convert_precision(tolerance: float) -> str | int:
    """Извлекает порядок точности

    :param tolerance: Порог точности, представленный числом с плавающей точкой.
    :return: Количество знаков после запятой для округления.

    # >>> convert_precision(0.001)
    # 3
    # >>> convert_precision(0.0001)
    # 4
    """
    if tolerance == 0:
        return "Tolerance cannot be zero."
    else:
        return abs(int(math.log10(abs(tolerance))))

