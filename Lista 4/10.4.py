def chop(lst):
    if len(lst) > 1:
        del lst[0]
        del lst[-1]

# Teste
t = [1, 2, 3, 4]
chop(t)
print(t)