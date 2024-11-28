from time import perf_counter
from calc import calculate


class BatchCalculatorContextManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        self.start_time = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.end_time = perf_counter()
        self.execution_time = self.end_time - self.start_time
        print(f"Execution time: {self.execution_time:.6f} seconds")

    def process_lines(self):
        for line in self.file:
            yield line.strip()


def parse_expression(expression):
    parts = expression.split(',')
    if len(parts) != 3:
        raise ValueError("Invalid expression format.")
    return parts[0], parts[1], parts[2]


def calc_with_manager(filename):
    with BatchCalculatorContextManager(filename) as manager:
        for line in manager.process_lines():
            try:
                operand1, operator, operand2 = parse_expression(line)
                print(f"Parsing result: {operand1}, {operator}, {operand2}")
                result = calculate(operand1, operator, operand2)
                print(f"Task: {line}")
                print(f"Result: {result}\n")
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    calc_with_manager('calcc.txt')