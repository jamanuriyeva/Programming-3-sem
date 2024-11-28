import random


class RandomNumberIterator:
    def __init__(self, params: list):
        self.params = params
        self.count = params[0]  # Количество чисел для генерации
        self.min_value = params[1]  # Минимальное значение диапазона
        self.max_value = params[2]  # Максимальное значение диапазона
        self.generated_numbers = []  # Список сгенерированных чисел

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.generated_numbers) < self.count:
            new_number = random.randint(self.min_value, self.max_value)
            self.generated_numbers.append(new_number)
            return new_number
        else:
            raise StopIteration

    def get_params(self):
        return self.params


def main():
    # Передаём параметры: количество чисел, минимальное и максимальное значение
    iterator = RandomNumberIterator([5, 10, 50])

    # Используем цикл for для вывода всех элементов генератора
    for number in iterator:
        print(number)


if __name__ == "__main__":
    main()