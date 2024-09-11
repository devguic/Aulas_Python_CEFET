def print_long_words(filename):
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            if len(word) > 20:
                print(word)


print_long_words('words.txt')