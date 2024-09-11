def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

def recurse(n, s):
    """
    Calcula e imprime recursivamente a soma de uma série.

    Esta função soma recursivamente a série decrementando 'n' e
    adicionando 'n' a 's' em cada passo. Quando 'n' atinge 0, ela imprime a soma acumulada 's'.

    Parâmetros:
    n (int): O inteiro inicial, que é decrementado por 1 em cada chamada recursiva.
    s (int): A soma acumulada, que é incrementada pelo valor atual de 'n' em cada chamada.

    Exemplo:
    recurse(3, 0) imprimirá 6 porque as chamadas são:
    recurse(3, 0) -> recurse(2, 3) -> recurse(1, 5) -> recurse(0, 6), que imprime 6.

    Nota:
    Se chamada com 'n' negativo, a função entrará em um loop recursivo infinito.
    Certifique-se de que 'n' é não-negativo antes de chamar esta função.
    """
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)