def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(48, 18)) 
print(gcd(56, 98))  
print(gcd(101, 10)) 
print(gcd(54, 24)) 