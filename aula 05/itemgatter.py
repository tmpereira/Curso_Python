'''
comando itemgetter
'''
import operator as op
lista =[('thiago',90,1.78),('maria',65,1.7),('mauricio',80,1.75)]
for i in lista:
    print(i)
ordenado = sorted(lista,key=op.itemgetter(0))
print(30*'=-')
print(ordenado)