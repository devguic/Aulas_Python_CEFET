num = input ("Escreva um número de 5 dígitos ")

def separa (num):
    digito_1 = num // 10000
    digito_2 = (num // 1000) % 10
    digito_3 = (num // 100) % 10
    digito_4 = (num// 10) % 10
    digito_5 = num % 10

    # Imprime os dígitos separados por três espaços cada
    print(f"{digito_1}   {digito_2}   {digito_3}   {digito_4}   {digito_5}")


num = int (input ("Escreva um número de 5 dígitos "))
ver = separa (num)

print (ver)