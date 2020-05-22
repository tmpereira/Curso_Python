num = int(input('digite um numero inteiro: '))
primo = True
for i in range(2,num):
    if ( num%i == 0):
        primo = False
if (primo):
    print(primo)
    print(f'o nomero {num} é um numero primo')
else:
    print(primo)
    print(f'o nomero {num} não é um numero primo')

