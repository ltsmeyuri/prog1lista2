v = float(input('Insira o valor da sua hora: '))
h = float(input('Insira a quantidade de horas trabalhadas no m�s: '))
sb = v*h

print ('Seu sal�rio bruto � de {} '.format(sb))
if sb<=900:
    ir= 0
    sindicato = sb *(3/100)
    inss = sb*(1/10)
    #fgts n�o � descontado do prolet�rio
    fgts = sb *(11/100)
    sl=sb - ir - sindicato - inss
    
    print ('(-)Imposto de Renda R$: {}'.format(ir))
    print ('(-)Sindicato R$: {}'.format(sindicato))
    print ('(-)INSS R$: {}'.format(inss))
    print ('FGTS R$: {}'.format(fgts))
    print ('Seu sal�rio liquido � R$: {}'.format(sl))
elif 900<sb<=1500:
    ir= sb * (1/20)
    sindicato = sb *(3/100)
    inss = sb*(1/10)
    #fgts n�o � descontado do prolet�rio
    fgts = sb *(11/100)
    sl=sb - ir - sindicato - inss
    
    print ('(-)Imposto de Renda R$: {}'.format(ir))
    print ('(-)Sindicato R$: {}'.format(sindicato))
    print ('(-)INSS R$: {}'.format(inss))
    print ('FGTS R$: {}'.format(fgts))
    print ('Seu sal�rio liquido � R$: {}'.format(sl))
elif 1500<sb<=2500:
    ir= sb *(1/10)
    sindicato = sb *(3/100)
    inss = sb*(1/10)
    #fgts n�o � descontado do prolet�rio
    fgts = sb *(11/100)
    sl=sb - ir - sindicato - inss
    
    print ('(-)Imposto de Renda R$: {}'.format(ir))
    print ('(-)Sindicato R$: {}'.format(sindicato))
    print ('(-)INSS R$: {}'.format(inss))
    print ('FGTS R$: {}'.format(fgts))
    print ('Seu sal�rio liquido � R$: {}'.format(sl))
else:
    ir= sb *(1/5)
    sindicato = sb *(3/100)
    inss = sb*(1/10)
    #fgts n�o � descontado do prolet�rio
    fgts = sb *(11/100)
    sl=sb - ir - sindicato - inss
    
    print ('(-)Imposto de Renda R$: {}'.format(ir))
    print ('(-)Sindicato R$: {}'.format(sindicato))
    print ('(-)INSS R$: {}'.format(inss))
    print ('FGTS R$: {}'.format(fgts))
    print ('Seu sal�rio liquido � R$: {}'.format(sl))