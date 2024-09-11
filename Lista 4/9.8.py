def is_palindrome(s):
    return s == s[::-1]

def find_odometer_reading():
    for n in range(100000, 1000000):  # de 100000 a 999999
        s = str(n)
        if (is_palindrome(s[2:6]) and
            is_palindrome(str(n + 1)[1:6]) and
            is_palindrome(str(n + 2)[1:5]) and
            is_palindrome(str(n + 3))):
            print(f"Odometer reading: {n}")

find_odometer_reading()