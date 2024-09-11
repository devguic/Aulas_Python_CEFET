def find_reverse_pairs(word_list):
    reverse_pairs = []
    word_set = set(word_list)
    for word in word_list:
        if word[::-1] in word_set and word != word[::-1]:
            reverse_pairs.append((word, word[::-1]))
    return reverse_pairs


word_list = ['evil', 'live', 'desserts', 'stressed', 'hello']
print(find_reverse_pairs(word_list))