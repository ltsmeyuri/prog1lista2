s = float(input('Insira a qtde, em KG, de morangos a ser adquirida pelo cliente: '))
a = float(input('Insira a qtde, em KG, de maçãs a ser adquirida pelo cliente: '))
kg = s+a
p = 0
if s<=5:
   p+= 2.5*s
else:
    p+= 2.2*s
if a<=5:
    p+= 1.8*a
else:
    p+=1.5*a
if kg>8 or p>25:
    p-= p/10
    
print ('A quantidade de morangos foi de {}, a de maçãs foi de {}, o preço é de R$: {}'.format(s,a,p))