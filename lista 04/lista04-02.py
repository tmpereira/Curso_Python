'''
Crie um programa onde o usuário possa digitar 10 valores
numéricos e cadastre-os em 2 listas separadas. Sendo a
primeira contendo números primos e segunda não
primos
'''

# determinando se é numero primo

primo = []
nprimo = []
for i in range(0,10):
    k = int(input('digite um numero inteirp'))
    # determinando se é numero primo
    p = True
    for i in range(2,k):
        if(k%i == 0):
            print(f'O numero {k} é não é primo')
            nprimo.append(k)
            p = False
            break
    if(p):
        print(f'o numero {k} é primo')
        primo.append(k)
print(' os numero primos digitados sao:')
print(primo)
print('os numeros não primos sao: ')
print(nprimo)