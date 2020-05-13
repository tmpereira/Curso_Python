'''
Crie um script em Python que solicite o nome, altura e peso
de uma pessoa e mostre a seguinte mensagem: “João tem
90 kilos e altura de 1.78 e portanto o IMC é de 28.4”


'''

nome = input('digite o nome do usuario')
altura = float(input('digite a altura da pessoa'))
peso = float(input('digite o peso do usuario'))
imc = peso / altura**2
print(f'{nome} tem {peso} kilos e altura de {altura:.2f} e portanto o IMC é de {imc:.2f}')
