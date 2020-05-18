'''
Escreva um programa que leia 3 números e que imprima o maior e o menor
'''
a = int(input('digite o primeiro número: '))
b = int(input('digite o segundo número: '))
c = int(input('digite o terceiro número: '))
if (a>b and a >c):
    maior = a
elif(b>a and b>c):
    maior = b
else:
    maior = c

if (a <b and a<c):
    menor = a
elif (b <c and b<a):
    menor = b
else:
    menor = c
print(f'o menor valor digitado é {menor} e o maior valor é {maior}')