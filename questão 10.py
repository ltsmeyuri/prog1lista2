x1=float(input('Insira sua primeira nota: '))
x2=float(input('Insira sua segunda nota: '))
x3=float(input('Insira sua terceira nota: '))
m = (x1+x2+x3)/3
if m>10 or m<0:
    print('Inválido.')
else:
    if m<7:
        print('Reprovado. Sua média foi {}'.format(m))
    elif 10>m>=7:
        print('Aprovado. Sua média foi {}'.format(m))
    else:
        print('Aprovado com distinção.')