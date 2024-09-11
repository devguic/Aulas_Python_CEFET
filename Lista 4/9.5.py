def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

def count_words_using_all_vowels(filename):
    count_aeiou = 0
    count_aeiouy = 0
    
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            if uses_all(word, "aeiou"):
                count_aeiou += 1
            if uses_all(word, "aeiouy"):
                count_aeiouy += 1
    
    print(f"Words using all 'aeiou': {count_aeiou}")
    print(f"Words using all 'aeiouy': {count_aeiouy}")

# Chame a função com o nome do arquivo
count_words_using_all_vowels('words.txt')