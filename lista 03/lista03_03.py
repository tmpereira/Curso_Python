'''
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem cobrando 0,50 por Km rodado para viagens até 200Km
e 0,45 para viagens mais longas.
'''
distancia = float(input('digite a distancia percorrida '))
if(distancia < 200):
    valor = distancia*0.5
    print(f'o valor da corrrida é de {valor} reais')
else:
    valor = distancia * 0.45
    print(f'o valor da corrrida é de {valor} reais')