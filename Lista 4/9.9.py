def find_reversible_ages():
    count = 0
    for child_age in range(1, 100):
        for mother_age in range(child_age + 1, 100):
            if str(child_age).zfill(2)[::-1] == str(mother_age).zfill(2):
                count += 1
                if count == 6:
                    initial_child_age = child_age
                if count == 8:
                    print(f"Child age now: {child_age}, Mother age now: {mother_age}")
                    return

find_reversible_ages()