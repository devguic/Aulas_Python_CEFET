def has_no_e(word):
    return 'e' not in word

def print_words_without_e(filename):
    total_words = 0
    words_without_e = 0
    
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            total_words += 1
            if has_no_e(word):
                print(word)
                words_without_e += 1
    
    percentage = (words_without_e / total_words) * 100
    print(f"Percentage of words without 'e': {percentage:.2f}%")

# Chame a função com o nome do arquivo
print_words_without_e('words.txt')