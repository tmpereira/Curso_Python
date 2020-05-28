'''
Faça um programa que leia o nome RA e média final de
um aluno. Armazene todas as informações num
dicionário. No final programa deve imprimir as
informações do dicionário e situação do aluno
(reprovado, exame ou aprovado). Utilize as regras da
UNIFESP para definir a situação do aluno.
'''
nome = input('digite o nome do aluno: ')
media = float(input('digite a media final do aluno'))
aluno ={
    'nome':nome,
    'media':media
}
print(aluno)
if(media < 3):
    print('o aluno esta reprovado')
elif(media > 6):
    print('o aluno esta aprovado')
else:
    print('o aluno esta de exame')
