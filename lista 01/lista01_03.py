'''
Escreva um script que leia a quantidade de dias,horas,
minutos e segundos para o usuário. Calcule o total em
segundos.
'''
dias = int(input('digite o numero de dias '))
horas = int(input('digite o numero de horas'))
minutos = int(input('digite o numero de minutos'))
segundos = int(input('digite o numero de segundos'))
dias_segs = 24*60*60*dias
horas_segs = 60*60*horas
minutos_segs = 60*minutos

total_segs = dias_segs+horas_segs+minutos_segs+segundos

print('no periodo de {} dias, {} horas, {} minutos e {} segundos possui o total de {} segundos'.format(dias,horas,minutos,segundos,total_segs))
