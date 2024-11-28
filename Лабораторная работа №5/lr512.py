import random

def rndm_gen(count, start, end):
    for i in range(count):
        yield random.randint(start, end)

for number in rndm_gen(5, 1, 12):
    print(number)