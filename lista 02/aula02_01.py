'''
Crie uma rotina que solicite ao usuário dois lados de um
triângulo e ângulo , em graus, entre eles e retorna o
comprimento do terceiro lado. Use a lei dos cossenos
'''


mport math as m
a = float(input('digite o valor do lado a do triangulo'))
b = float(input('digite o valor do lado b do triangulo'))
angle = float(input('digite o angulo em graus'))
angle = m.pi*angle/180
c = m.sqrt((a**2)+(b**2)-(2*a*b*m.cos(angle)))
print(f'o valor de lado c é {c:.3f}')