'''
Faça um programa que calcule a soma os números impares e múltiplos de 3
que se encontram no intervalo de 1 até 500
'''

soma = 0
for i in range(1,501):
    if(i%2 == 1 and i%3 == 0):
        soma = soma + i
        print(f'o numero {i} foi selecionado ')
print(f'o valor da soma dos 500 primeiros numeros impares e divisivel por 3 é {soma}')