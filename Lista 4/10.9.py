import time

def read_words_append(filename):
    word_list = []
    with open(filename, 'r') as file:
        for line in file:
            word_list.append(line.strip())
    return word_list

def read_words_concat(filename):
    word_list = []
    with open(filename, 'r') as file:
        for line in file:
            word_list = word_list + [line.strip()]
    return word_list

# Teste de desempenho
start = time.time()
read_words_append('words.txt')
print("Tempo usando append:", time.time() - start)

start = time.time()
read_words_concat('words.txt')
print("Tempo usando concatenação:", time.time() - start)