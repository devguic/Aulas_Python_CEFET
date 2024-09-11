def cumsum(lst):
    cumulative_sum = []
    total = 0
    for num in lst:
        total += num
        cumulative_sum.append(total)
    return cumulative_sum

# Teste
t = [1, 2, 3]
print(cumsum(t))