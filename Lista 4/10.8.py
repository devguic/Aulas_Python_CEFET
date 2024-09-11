import random

def has_matching_birthdays(num_students):
    birthdays = [random.randint(1, 365) for _ in range(num_students)]
    return has_duplicates(birthdays)

def birthday_paradox_simulation(num_students, num_simulations):
    matches = 0
    for _ in range(num_simulations):
        if has_matching_birthdays(num_students):
            matches += 1
    return matches / num_simulations


print(birthday_paradox_simulation(23, 10000)) 