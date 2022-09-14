a = float(input('Esse programa calculará as raizes de uma equação quadrática. Insira o valor correspondente ao a: '))
b = float(input('Ao b: '))
c = float(input('Ao c: '))
if a == 0:
    print('Os valores informados não correspondem a uma equação do segundo grau. ')
else:
    d = (b**2) - (4 * a * c)
    if d < 0:
        print(d)
        print('Delta com valor negativo. Não há raizes reais.')
    elif d == 0:
        x = -b/(2*a)
        print('A raíz é {}'.format(x))
    else:
        x1 = (-b + (d**(1/2)))/(2*a)
        x2 = (-b - (d**(1/2)))/(2*a)
        
        print('A primeira raíz é {} e a segunda é {}.'.format(x1,x2))
