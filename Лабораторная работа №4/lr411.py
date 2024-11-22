lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 13
def two_sum(lst, target):
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                res = [i, j]
                return res
    return res


print(two_sum(lst, target))

