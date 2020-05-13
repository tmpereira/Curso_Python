'''
rie uma rotina que solicite uma frase ao usuário e retorne
o número de caracteres na frase e o número de espaços.
'''
frase = input('digite uma frase').strip()
tamanho = len(frase)
nspace = frase.count(' ')
print(f' a frase digitada possui {tamanho} caracteres