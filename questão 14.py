n1 = float(input('Insira um número: '))
n2 = float(input('Insira outro número: '))
op = str(input('Insira se a operação é soma, subtração, divisão ou multiplicação: '))

if op == 'soma':
    calc=n1+n2
elif op == 'subtração':
    calc=n1-n2
elif op == 'divisão':
    calc ==n1/n2
elif op == 'multiplicação':
    calc=n1*n2
else:
    print('Inválido')
print('O resultado da operação é: {}'.format(calc))
if calc>0:
    print('Esse número é positivo.')
elif calc==0:
    print('Esse número é zero.')
else:
    print('Esse número é negativo.')
if calc-int(calc)==0:
    print('Esse número é inteiro.')
else:
    print('Esse número é decimal.;')