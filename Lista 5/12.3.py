def pares_metatese(palavras):
    anagramas = {}
    for palavra in palavras:
        palavra_ordenada = ''.join(sorted(palavra))
        if palavra_ordenada in anagramas:
            anagramas[palavra_ordenada].append(palavra)
        else:
            anagramas[palavra_ordenada] = [palavra]

    def e_metatese(palavra1, palavra2):
        contagem = 0
        for c1, c2 in zip(palavra1, palavra2):
            if c1 != c2:
                contagem += 1
            if contagem > 2:
                return False
        return contagem == 2

    for grupo in anagramas.values():
        for i in range(len(grupo)):
            for j in range(i + 1, len(grupo)):
                if e_metatese(grupo[i], grupo[j]):
                    print(grupo[i], grupo[j])

palavras = ['conversa', 'conserva', 'silente', 'enlistar']
pares_metatese(palavras)
