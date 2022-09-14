dd=int(input('Insira uma data. Dia: '))
mm=int(input('Insira o mês: '))
aaaa=int(input('Insira o ano: '))

if 0<dd<=31 and 0<mm<=12:
    print('A data é válida.')
else:
    print('A data não é válida.')