T = str(input('Insira o tipo de combustível que o cliente escolheu: '))
V = float(input('Insira a quantidade, em litros, de combustível a ser abastecida: '))

if T == 'Álcool':
    if V<=20:
        valor = (V*1.9)-((int(V)*1.9)*(3/100))
    else:
        valor = (V*1.9)-((int(V)*1.9)*(5/100))
if T == 'Gasolina':
    if V<=20:
        valor = (V*2.5)-((int(V)*2.5)*(4/100))
    else:
        valor = (V*2.5)-((int(V)*2.5)*(6/100))
valor = round(valor,2)

print ('O valor a ser pago é R$ {} '.format(valor))