ndias = int(input('digite o numero de dias na qual o carro ficará alugado'))
km_rodado = float(input('digite a distancia rodado durante o periodo'))
preço_aluguel = ndias*60 + 0.15*km_rodado
print(f'o valor total do alugel é de {preço_aluguel:.2f} reais')