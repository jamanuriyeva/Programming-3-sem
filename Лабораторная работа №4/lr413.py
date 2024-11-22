lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8

def two_sum_hashed_all(lst, target):
    hashed = {}
    results = []

    for index, value in enumerate(lst):
        comp = target - value
        if comp in hashed:
            for prev_index in hashed[comp]:
                results.append((prev_index, index))
        if value not in hashed:
            hashed[value] = []
        hashed[value].append(index)

    return results

result = two_sum_hashed_all(lst, target)
print(result)