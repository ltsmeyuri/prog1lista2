a = float(input('Insira sua primeira nota: '))
b = float(input('Insira sua segunda nota: '))
m = (a+b)/2

if 0<=m<4:
    
    print('A média de suas notas é de {}'.format(m))
    print('Seu conceito é E. Você foi reprovado :).')
elif 4<=m<6:
    
    print('A média de suas notas é de {}'.format(m))
    print('Seu conceito é D. Você foi reprovado :).')
elif 6<=m<7.5:
    
    print('A média de suas notas é de {}'.format(m))
    print('Seu conceito é C. Você foi aprovado :).')
elif 7.5<=m<9:
    
    print('A média de suas notas é de {}'.format(m))
    print('Seu conceito é B. Você foi aprovado :).')
else:
    
    print('A média de suas notas é de {}'.format(m))
    print('Seu conceito é A. Você foi aprovado :).')