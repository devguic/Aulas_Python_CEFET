def nested_sum(lst):
    total = 0
    for sublist in lst:
        total += sum(sublist)
    return total

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t)) 