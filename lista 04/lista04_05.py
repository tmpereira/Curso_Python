'''
Crie um programa que leia nome, sexo, peso e altura de
várias pessoas. guarde os dados de cada pessoa num
dicionário individual e acrescente o IMC da pessoa.
Organize todos os dicionários em uma lista. No final
mostre
a. Quantas pessoas foram cadastradas
b. Qual é o peso médio das pessoas
c. Qual é a altura média das pessoas
d. Qual é IMC médio das pessoas
'''
npessoas = int(input('digite a quantidade de pesssoas que deseja cadastrar: '))
lista =[]
pessoa ={}
saltura = speso = simc = 0
for i in range(0,npessoas):
    print(f'digite as informações da {i+1} pessoa ')
    pessoa['nome'] = input('digite o nome da pessoa: ')
    pessoa['sexo'] = input('digite o sexo da pessoa: ')
    pessoa['peso'] = float(input('digite o peso da pessoa'))
    speso += pessoa['peso']
    pessoa['altura'] = float(input('digite a altura da pessoa'))
    saltura += pessoa['altura']
    pessoa['IMC'] = pessoa['peso']/(pessoa['altura']**2)
    simc += pessoa['IMC']
    lista.append(pessoa.copy())

print(20*'-')
for i in lista:
    for j,k in i.items():
        print(f'{j} é {k}')
    print(20*'-')
print(f'foram cadastradas {len(lista)} pessoas')
print(f'o peso medio das pessoas é {speso/len(lista):.2f}')
print(f'o imc medio das pessoas é {simc/len(lista):.2f}')
print(f'a altura media é {saltura/len(lista):.2f}')
