"""
    Tipo Numerico
"""


nome1 = 'UTFPR Toledo Universidade'
nome = "Diego"
print(nome.split())

print(nome.split()[0])
print(nome.split()[0][0])
print(nome.split()[0][1])


print("Tudo ao contrario")
print(nome[::-1])

print("\n")

idade = int(input(f'{nome} me conta tua idade \n'))

if idade < 18:
    print(f'{nome} ainda nao pode tirar a CNH \n')
elif 18 < idade < 40:
    print(f'{nome}, okey podemos dar seguimento na CNH \n')
elif 40 < idade < 58:
    print(f'{nome}, bom teremos que fazer alguns exames para dar continuidade \n')
else:
    print(f'{nome} talvez seja possivem manter a CNH ainda mas vai depender da avaliacao do medico \n')

ativo = True
logado = False


if ativo or logado:
    print(f'{nome} esta logado')
else:
    print(f'{nome} nao esta logado')

if not ativo:
    print(f'{nome} precisa ativar tua conta')
else:
    print(f'{nome} bem vindo ao sistema ')
