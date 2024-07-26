import math



def comprimento (raio):
    x = 2 * raio * math.pi
    return (x)

def area (raio):
    y = math.pi * raio ** 2
    return (y) 


pergunta = input ("Qual é o raio da circunferência? ")
raio = float (pergunta)


cc = comprimento(raio)
aa = area(raio)

print (cc)
print (aa)