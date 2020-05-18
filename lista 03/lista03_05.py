'''
Desenvolva um programa que solicite  o primeiro número de uma PA e sua razão.
O programa deve imprimir os 10 primeiros termos.
'''
P_numero = int(input('dighite o primeiro termo da PA: '))
razao = float(input('digite a razão da PA: '))
for i in range(0,10):
    n_termo = P_numero + i*razao
    print(f'o {i+1} termo da PA é {n_termo}')