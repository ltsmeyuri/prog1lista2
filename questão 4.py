a = float(input('Insira sua primeira nota: '))
b = float(input('Insira sua segunda nota: '))
m = (a+b)/2

if 0<=m<4:
    
    print('A m�dia de suas notas � de {}'.format(m))
    print('Seu conceito � E. Voc� foi reprovado :).')
elif 4<=m<6:
    
    print('A m�dia de suas notas � de {}'.format(m))
    print('Seu conceito � D. Voc� foi reprovado :).')
elif 6<=m<7.5:
    
    print('A m�dia de suas notas � de {}'.format(m))
    print('Seu conceito � C. Voc� foi aprovado :).')
elif 7.5<=m<9:
    
    print('A m�dia de suas notas � de {}'.format(m))
    print('Seu conceito � B. Voc� foi aprovado :).')
else:
    
    print('A m�dia de suas notas � de {}'.format(m))
    print('Seu conceito � A. Voc� foi aprovado :).')