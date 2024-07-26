
def check_fermat (a, b, c, n):
    x =  a**n + b**n
    if (n > 2 & x == c*n):
        print ("Holy smokes, Fermat was wrong!")
    else:
        print ('No, that doesn’t work.')
    if (n <2):
        print("Não se aplica, n < 2")


a = int(input("Escreva o valor de a: "))
b = int(input("Escreva o valor de b: "))
c = int(input("Escreva o valor de c: "))
n = int(input("Escreva o valor de n: "))

check_fermat(a, b, c, n)