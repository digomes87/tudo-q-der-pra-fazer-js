"""
    Lambada
    funcoes lambdas sao funcoes anonimas
"""

# funcao norma
def funcao(x):
    return x * 3 + 4

print(funcao(5))


# Expressao Lambda
calc = lambda x: x * 3 + 4
print(calc(5))

autores = ['Isaac Asimov', 'Ray bradburry','Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card', 'H. G. Wells']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

print("Versao F and C graus")
print("Famoso, chamando no grau !!")

cidades = [('Berlim', 29), ('Brazil', 34), ('Japao', 23), ('Dublin', 6), ('Italia', 2)]
print(cidades)
c_para_f = lambda dado: (dado[0], (9/5) * dado[1]+32)
print("Mostrando os dois resultados")
print(list(map(c_para_f, cidades)))
