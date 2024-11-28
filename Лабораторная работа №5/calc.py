def calculate(operand1, operator, operand2):
    # Преобразуем строки в числа
    op1 = float(operand1)
    op2 = float(operand2)

    # Определяем операцию и выполняем её
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        if op2 == 0:
            raise ZeroDivisionError("Деление на ноль!")
        return op1 / op2
    else:
        raise ValueError(f"Недопустимый оператор: '{operator}'")