def is_power(a, b):
    if a == b:
        return True

    elif a == 1:
        return True

    elif a % b != 0:
        return False

    else:
        return is_power(a // b, b)


print(is_power(8, 2))  
print(is_power(27, 3))   
print(is_power(10, 2))   
print(is_power(1, 5))   
print(is_power(81, 3))   