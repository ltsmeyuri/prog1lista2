a = int(input('Insira um dia da semana, considerando que 1 é segunda-feira e 7 domingo, e que os valores do meio seguem a lógica respectiva: '))
if a == 1:
    print('É segunda-feira.')
elif a == 2:
    print('É terça-feira.')
elif a == 3:
    print('É quarta-feira.')
elif a == 4:
    print('É quinta-feira.')
elif a == 5:
    print('É sexta-feira.')
elif a == 6:
    print('É sábado.')
elif a == 7:
    print('É domingo.')
else:
    print('Valor inválido.')