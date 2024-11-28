def fibon():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

def ten_fib(fib_gen):
    for n in fib_gen:
        yield n + 10


gen = fibon()
ten_gen = ten_fib(gen)

k = 6

for i in range(k):
    print(next(ten_gen))