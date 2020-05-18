'''
Escreva um programa que pergunte a velocidade do carro de um usuário.
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
Nesse caso, exiba o valor da multa, cobrando 5 reais por Km acima de 80Km/h.
'''
vel = float(input('digite a velocidade do veiculo: '))

if (vel > 80):
    multa = (vel-80)*5
    print(f'o veiculo esta acima da velocidade permitida. a multa será de {multa} reais ')
else:
    print('o veiculo esta dentro da velocidade permitida')