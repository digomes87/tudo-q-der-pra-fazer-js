"""
    Loop No python é tudo de bom

"""

nome = 'Diego Go'
lista = [1, 2, 3, 4, 4, 5, 54, 2, 1]
numeros = range(1, 10)

for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

for numero in range(1, 10):
    print(numero)

print("====================")
for i, v in enumerate(nome):
    print(nome)

print("É Possivel descartar o indice com underline")
for _, v in enumerate(nome):
    print(nome)  # imprime o nome completo porem em formato de lista
    print(nome[1])  # imprime a posicao especifica da lista

qtd = int(input("Passa um número aí: \n"))

for n in range(1, qtd + 1):
    print(f'Imprimindo {n}')

resposta = ''
while resposta != 'sim':
    resposta = input(print("Já acabou Jessica ?"))

for numero in range(1, 10):
    if numero == 7:
        break
    else:
        print(numero)
print('Fora do Loop')

# exemplo 2
while True:
    comando = input("Digite sair para sair")
    if comando == 'sair':
        break
