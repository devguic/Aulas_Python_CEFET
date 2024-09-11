def in_bisect(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Teste
sorted_list = ['apple', 'banana', 'cherry', 'date', 'fig']
print(in_bisect(sorted_list, 'cherry'))
print(in_bisect(sorted_list, 'grape'))   