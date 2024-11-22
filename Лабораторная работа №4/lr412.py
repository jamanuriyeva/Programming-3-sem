lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 13
hashed = {}
def two_sum_hashed(lst, target):
    hashed = {}
    for index, value in enumerate(lst):
        comp = target - value
        if comp in hashed:
            return (hashed[comp], index)
        hashed[value] = index
    return None

result = two_sum_hashed(lst, target)
print(result)