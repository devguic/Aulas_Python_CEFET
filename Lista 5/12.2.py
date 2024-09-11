def encontrar_anagramas(arquivo):
    anagramas = {}
    with open(arquivo) as arquivo_palavras:
        for palavra in arquivo_palavras:
            palavra = palavra.strip().lower()
            palavra_ordenada = ''.join(sorted(palavra))
            if palavra_ordenada in anagramas:
                anagramas[palavra_ordenada].append(palavra)
            else:
                anagramas[palavra_ordenada] = [palavra]

    for grupo in sorted(anagramas.values(), key=len, reverse=True):
        if len(grupo) > 1:
            print(grupo)

encontrar_anagramas('palavras.txt')
