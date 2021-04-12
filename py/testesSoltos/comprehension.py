"""
    List Comprehesion

"""

numero_dobrado = []

for numero in [1, 2, 3, 4, 5]:
    numero_dobrado.append(numero * 3)

print(numero_dobrado)

# Aqui a List Comprehesion, resumi tudo em uma linha
print([numero * 2 for numero in [1, 3, 5, 6, 8]])

# tabuada
print([numero * 3 for numero in range(1, 10)])

# Outro exemplo
n = [1, 2, 3, 4 , 5,  6,  7, 8, 9, 10]

par = [numero for numero in n  if numero % 2 == 0]
impar = [numero for numero in n if numero % 2 != 0]

print(par)
print(impar)

# refactor
pares = [numero for numero in n if not numero % 2]
imparr = [numero for numero in n if numero % 2]

print(pares)
print(imparr)
