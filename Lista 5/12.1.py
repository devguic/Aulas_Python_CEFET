import string

def mais_frequente(texto):
    freq_letras = {}
    for caractere in texto:
        if caractere in string.ascii_letters:
            caractere = caractere.lower()
            freq_letras[caractere] = freq_letras.get(caractere, 0) + 1

    letras_ordenadas = sorted(freq_letras, key=freq_letras.get, reverse=True)
    for letra in letras_ordenadas:
        print(letra, freq_letras[letra])

texto = "Este é um exemplo de texto em português"
mais_frequente(texto)
