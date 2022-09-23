n=0
a = str(input('Esse programa analisará respostas para emitir um parecer sobre a relação ou não de uma pessoa com o crime. Responda com "sim" ou "não". Telefonou pra vítima? '))
b = str(input('Esteve no local do crime? '))
c = str(input('Mora perto da vítima? '))
d = str(input('Devia para a vítima?'))
e = str(input('Já trabalhou com a vítima?'))

if a == 'sim':
    n +=1
if b == 'sim':
    n +=1
if c == 'sim':
    n +=1
if d == 'sim':
    n +=1
if e == 'sim':
    n +=1
    
if n==2:
    print('A pessoa é suspeita.')
elif n==3 or n==4:
    print('A pessoa é cúmplice.')
elif n==5:
    print('A pessoa é o assassino.')
else:
    print('A pessoa é inocente.')