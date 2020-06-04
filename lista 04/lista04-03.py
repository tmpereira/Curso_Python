'''
Crie um programa que crie uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado. No final,
mostre a matriz na tela com a formatação correta.
'''

mat = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        mat[i][j] = float(input(f'digite o numero da posição [{i},{j}]'))

print('terminou a digitação da matriz')

for i in range(0,3):
    for j in range(0,3):
        print(f'[ {mat[i][j]} ] ', end='')
    print('')
