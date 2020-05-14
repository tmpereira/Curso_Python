'''
Faça um programa que leia a largura e a altura de uma parede em metros.
Calcule a sua área e a quantidade de tinta necessária para pinta-la.
Sabe-se que cada litro de tinta pinta uma área de 3 m2
'''

largura = float(input('digite a largura da parede'))
altura = float(input('digite a altura da parede'))
area = altura*largura
qtd_tinta = area/3

print(f' a quantidade de tinta necessaria para pintar uma parede de {altura} altura e {largura} largura é {qtd_tinta:.2f} litros')