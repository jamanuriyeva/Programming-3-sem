def fib_lst(n):
    f_lst = {0: 0, 1: 1}

    def _fibonacci(n):
        if n in f_lst:
            return f_lst[n]

        result = _fibonacci(n - 1) + _fibonacci(n - 2)
        f_lst[n] = result
        return result

    return _fibonacci(n)
print(fib_lst(10))

from functools import lru_cache

@lru_cache
def fib_lst(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_lst(n-1) + fib_lst(n-2)

print(fib_lst(10))






