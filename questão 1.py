s = float(input('Insira seu sal�rio para o c�lculo do reajuste:'))
if s<=280:
    print('Seu sal�rio era {}, teve um aumento de 20%, o que implicou um aumento de {}, resultando em um novo sal�rio de R$: {}'.format(s,s*2/10,s+(s*2/10)))
elif 280<s<=700:
    print('Seu sal�rio era {}, teve um aumento de 15%, o que implicou um aumento de {}, resultando em um novo sal�rio de R$: {}'.format(s,s*15/100,s+(s*15/100)))
elif 700<s<=1500:
    print('Seu sal�rio era {}, teve um aumento de 10%, o que implicou um aumento de {}, resultando em um novo sal�rio de R$: {}'.format(s,s*1/10,s+(s*1/10)))
else: 
    print('Seu sal�rio era {}, teve um aumento de 5%, o que implicou um aumento de {}, resultando em um novo sal�rio de R$: {}'.format(s,s*5/100,s+(s*5/100)))