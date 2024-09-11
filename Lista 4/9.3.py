def avoids(word, forbidden):
    for letter in forbidden:
        if letter in word:
            return False
    return True

def count_words_without_forbidden_letters(filename):
    forbidden = input("Enter forbidden letters: ")
    count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            if avoids(word, forbidden):
                count += 1
    
    print(f"Number of words without forbidden letters: {count}")

# Chame a função com o nome do arquivo
count_words_without_forbidden_letters('words.txt')