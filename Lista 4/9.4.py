def uses_only(word, allowed):
    for letter in word:
        if letter not in allowed:
            return False
    return True

# Testando a função com a série de letras "acefhlo"
print(uses_only("hoe", "acefhlo"))  # True
print(uses_only("alfalfa", "acefhlo"))  # True