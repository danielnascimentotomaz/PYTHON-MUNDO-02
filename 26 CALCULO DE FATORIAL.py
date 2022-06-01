"""
 Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120

"""

num = int(input('digite um numero para calcular seu fatorial:'))
f = 1

print('CALCULANDO O FATORIAL {}! ='.format(num), end=' ')
while num > 0:
    print(num, end=' ')

    if num > 1:
        print("x", end=" ")
    else:
        print("=", end=" ")

    f = f * num
    num = num - 1

print('{}'.format(f))



"""from math import factorial

num = int(input('DIGITE UM NUMERO PARA CALCULAR SEU FATORIAL:'))

fatorial = factorial(num)

print('O FATORIAL DE {} É {}'.format(num, fatorial))"""
