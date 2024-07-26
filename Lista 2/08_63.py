def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(first("abacate"))  #  'a'
print(last("abacate"))   #  'e'
print(middle("abacate")) #'bacat'

print(middle("ab"))      # ''
print(middle("a"))       # ''
print(middle(''))        # ''


print(is_palindrome("osso"))     # True
print(is_palindrome("reviver"))  #  True
print(is_palindrome("palavra"))  #  False
print(is_palindrome("a"))        #  True
print(is_palindrome(""))         # True