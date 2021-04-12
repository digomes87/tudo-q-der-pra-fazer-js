# aqui já temos uma lista
type([])

lista1 = [1, 2, 3, 4, 5, 6, 7, 'Diego', 8, 90]
lista2 = ['A', 'B', 'C', 'D']
lista3 = list(range(1, 11))
lista4 = list("ABCDEFGHIJeEEEeee")
lista5 = [2, 432, 12, 54, 65, 3, 56, 234, 24432, 1121]

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

lista5.sort()
print(lista5)

for item in lista4:
    item.lower()
    print(item)

muitaspalavras = "Aqui uma frase grande e cheia de erros que podem ser corrigidos"
print(muitaspalavras)
muitaspalavras = muitaspalavras.split()
print(muitaspalavras)

outraFrase = "Aqui uma frase, com, muitas, virgulas, que nao, deveriam existir"
outraFrase = outraFrase.split(',')
print(outraFrase)

# converter lista para string
lista6 = ["aqui", '12', "outra", "lista", "porem essa transformamos em string com join"]
lista6 = ' '.join(lista6)
# lista6 = '--'.join(lista6)
print(lista6)

carrinho = []
produto = ''

# while produto != 'sair':
#     print("Adicione algum produto a lista ou digite sair para encerrar: ")
#     produto = input()
#     if produto != 'sair':
#         carrinho.append(produto)
#
# for produto in carrinho:
#     print(produto)
#
cores = ["branco", "azul", "preto", "marrom"]

for indice, cor in enumerate(cores):
    print(indice, cor)
