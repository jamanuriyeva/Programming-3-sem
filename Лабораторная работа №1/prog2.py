#Задание 3.2

def GuessNumber(target, low, high):
    """
    :param target: загаданное число
    :param low: нижняя граница промежутка
    :param high: верхняя граница промежутка
    :return: выводит правильное число и количество попыток
    """
    count = 0
    while True:
        count += 1
        if low > high:
            return None, count
        guess = (low + high) // 2
        if guess == target:
            return guess, count
        elif guess < target:
            low = guess + 1
        else:
            high = guess - 1
    return None, count

target = int(input('Загадайте число\n'))
low = 0
high = 50
result, count = GuessNumber(target, low, high)
if result is not None:
    print(f"Загаданное число: {result}")
    print(f"Количество попыток: {count}")
else:
    print("Невозможно угадать число(.")