def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

# Teste
print(is_anagram('listen', 'silent')) 
print(is_anagram('hello', 'world')) 