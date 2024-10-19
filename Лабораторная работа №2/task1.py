def car():
    """
    Функция car внешняя функция, возвращает вложенную функцию inner_car

    :param year: int год
    :param model: str модель
    :param brand: str бренд

    """

    year = 2017
    model = "cls 63 amg"
    brand = 'Mercedes-Benz'

    def inner_car():
        """
        Функция  inner_car, возвращает словарь с брендом, моделью и годом изготовления машины

        :param year: int год
        :param model: str модель
        :param brand: str бренд

        """
        return {'year': year, 'model': model, 'brand': brand}

    return inner_car()


print(car())
