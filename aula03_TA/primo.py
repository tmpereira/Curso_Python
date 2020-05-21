num = int(input('digite um numero'))
primo = False
for i in range(2,num):
    if (num%i == 0):
        primo = True
    print(primo)

if (not primo):
    print('o numero digitado é um numero primo')
else:
    print('o numero digitado não é primo')
