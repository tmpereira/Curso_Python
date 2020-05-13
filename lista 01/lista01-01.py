nome = input('digite o nome do usuario')
altura = float(input('digite a altura da pessoa'))
peso = float(input('digite o peso do usuario'))
imc = peso / altura**2
print(f'{nome} tem {peso} kilos e altura de {altura:.2f} e portanto o IMC é de {imc:.2f}')
