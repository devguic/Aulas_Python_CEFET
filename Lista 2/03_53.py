def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Yes")
    else:
        print("No")

def tamanhograveto():
    a = int(input("Digite o comprimento do primeiro graveto: "))
    b = int(input("Digite o comprimento do segundo graveto: "))
    c = int(input("Digite o comprimento do terceiro graveto: "))
    is_triangle(a, b, c)

tamanhograveto()