import logging

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

def test_calcul():
    assert(3, 4, "+") == 7
    assert (5, 4, "-") == 1
    assert (3, 4, "*") == 12
    assert (10, 2, "/") == 0
    assert (3, 0, "/") == "You can't divide by zero!"


#def main():
    # num1 = int(input("Введите первое число: "))
    # num2 = int(input("Введите второе число: "))
    # operator = input("Выберите действие ('+', '/', '*'): ")
    # result = calculate(num1, num2, operator)
    # print(result)

def rounded_res():
    rounded_result = round.result()
#main()


