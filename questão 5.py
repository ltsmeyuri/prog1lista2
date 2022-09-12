a = float(input('Insira três valores para lados de um triângulo. Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))
if a+b<c or b+c<a or a+c<b:
    print('Os lados não podem formar um triângulo.')
elif a == b == c:
    print('Os lados formam um triângulo equilátero.')
elif a == b or a == c or b == c:
    print ('Os lados formam um triângulo isósceles.')
else:
    print ('Os lados formam um triângulo escaleno.')
    