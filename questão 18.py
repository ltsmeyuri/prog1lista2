t = int(input('Insira 1 para Filé Duplo, 2 para Alcatra ou 3 para picanha: '))
m = float(input('Insira, em KG, a qtde de carne a ser comprada: '))
c = int(input('A compra será no cartão do mercado? 1 para sim e 2 para não.'))              
v = 0
if t == 1:
    if m<=5:
        v+= 4.9*m
    else:
        v+= 5.8*m
elif t == 2:
    if m<=5:
        v+= 5.9*m
    else:
        v+= 6.8*m
elif t == 3:
    if m<=5:
        v+= 6.9*m
    else:
        v+= 7.8*m
if c == 1:
    v -= v/20