a = int(input('Insira um ano e esse programa dirá se é ou não bissexto: '))
if a%4==0:
    print('O ano {} é bissexto.'.format(a))
else:
    print('O ano {} não é bissexto.'.format(a))