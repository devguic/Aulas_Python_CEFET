def has_three_consecutive_doubles(word):
    count = 0
    i = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count += 1
            i += 2
            if count == 3:
                return True
        else:
            count = 0
            i += 1
    return False

def find_word_with_three_doubles(filename):
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            if has_three_consecutive_doubles(word):
                print(word)
                break  # Se você deseja encontrar todas as palavras, remova esta linha

# Chame a função com o nome do arquivo
find_word_with_three_doubles('words.txt')