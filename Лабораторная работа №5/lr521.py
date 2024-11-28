import time

class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time
        print(f"Время выполнения: {self.elapsed_time:.6f} секунд.")

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

def main():
    n = 1000000
    with Timer():
        for i in fibonacci(n):
            pass

if __name__ == "__main__":
    main()