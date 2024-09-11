def is_interlock(word1, word2, combined):
    return ''.join(word1[i // 2] if i % 2 == 0 else word2[i // 2] for i in range(len(combined))) == combined

def find_interlocking_words(word_list):
    interlocks = []
    word_set = set(word_list)
    for word in word_list:
        if len(word) % 2 == 0:
            part1 = word[::2]
            part2 = word[1::2]
            if part1 in word_set and part2 in word_set:
                interlocks.append((part1, part2, word))
    return interlocks


word_list = ['shoe', 'cold', 'schooled', 'gold']
print(find_interlocking_words(word_list))