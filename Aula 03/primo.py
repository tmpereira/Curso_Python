n = int(input('digite um numero inteiro'))
primo = True
for i in range(2,n):
    if (n%i == 0):
        primo = False
if(primo):
    print(f'o numero {n} é primo')
else:
    print(f'o numero {n} não é primo')

