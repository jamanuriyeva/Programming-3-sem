def car():
    year = 2017
    model = "cls 63 amg"
    brand = 'Mercedes-Benz'

    def inner_car():
        return {'year': year, 'model': model, 'brand': brand}

    return inner_car()


print(car())
