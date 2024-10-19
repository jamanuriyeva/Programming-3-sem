#Задание 3.1
def calculate(num1, num2, operator):
    """
    :param num1: первое число
    :param num2: второе число
    :param operator: дествие, которое будет выполняться с числами
    :return: выводит результат математического действия
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

# def test_calcul():
#     assert calculate(3, 4, "+") == 7
#     assert calculate(5, 4, "-") == 1
#     assert calculate(3, 4, "*") == 12
#     assert calculate(10, 2, "/") == 0
#     assert calculate(3, 0, "/") == "You can't divide by zero!"

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Choose operation (+, -, *, /): ")
    result = calculate(num1, num2, operator)
    print(f"Result: {result}")

main()
