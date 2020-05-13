'''Faça um script que calcule o aumento de salário. Ele deve
solicitar o valor do salário e a porcentagem de aumento.
Exiba o valor do aumento e do novo salário
'''
salario = float(input('digite o valor do salario: '))
aumento = float(input('digite o aumento porcentual do salario'))
aumento = aumento/100
novo_salario = salario*(1+aumento)
print('o valor do novo salario será de: {}'.format(novo_salario