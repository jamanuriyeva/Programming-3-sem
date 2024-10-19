from functools import partial
radioactive_funcs = {"Ru_103": None, "Ru_106": None}

def calculate_remaining_amount(N0, t, t1_half):
    """Расчитывает остаток радиоактивного вещества.
    :param N0: количество радиоактивного вещества до распада
    :type N0: int
    :param t: время
    :type t: int
    :param t1_half: период полураспада
    :type t1_half: int
    """
    return N0 * pow(0.5, t / t1_half)


def f1(N0, t, t1_half):

    res = f"Масса радиоактивного вещества Ru_103, t1_2={t1_half}"
    result = calculate_remaining_amount(N0, t, t1_half)
    print(
        f'{res} с периодом полураспада {t1_half}, N0 = {N0}, t={t}, осталось вещества: {result}'
    )
    return result


def f2(N0, t, t1_half):
    res = f"Масса радиоактивного вещества Ru_106, t1_2={t1_half}"
    result = calculate_remaining_amount(N0, t, t1_half)
    print(
        f'{res} с периодом полураспада {t1_half}, N0 = {N0}, t={t}, осталось вещества: {result}'
    )
    return result


def main():
    t1_2_elems = {"Ru_103": 39, "Ru_106": 368}
    """ каррированные функции для каждого изотопа"""
    radioactive_funcs["Ru_103"] = partial(f1, t1_half=t1_2_elems["Ru_103"])
    radioactive_funcs["Ru_106"] = partial(f2, t1_half=t1_2_elems["Ru_106"])

    N0 = 100
    t = 10

    for key in radioactive_funcs:
        print(f"Результаты для {key}:")
        print(radioactive_funcs[key](N0, t))


main()