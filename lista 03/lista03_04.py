'''
Escreva um programa que pergunte o deposito inicial e a taxa de Juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses.
No final deve imprimir o total de ganho com juros no período.
'''
depot = float(input('digite o valor inicial colocado na poupança: '))
taxa_juros = float(input('digite a taxa de juros em %'))
taxa_juros = 1 + taxa_juros/100
print(f'o valor no mes 0 é de {depot} reais')
for i in range(1,25):
    depot = depot*taxa_juros
    print(f'o valor no mes {i} é de {depot:.2f} reais')
