def is_abecedarian(word):
    previous = word[0]
    for letter in word:
        if letter < previous:
            return False
        previous = letter
    return True

def count_abecedarian_words(filename):
    count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            if is_abecedarian(word):
                count += 1
    
    print(f"Number of abecedarian words: {count}")

# Chame a função com o nome do arquivo
count_abecedarian_words('words.txt')