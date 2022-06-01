"""17) Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

numero = int(input('DIGITE UM NÚMERO:'))

count = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[0;33m', end=' ')
        count = count + 1
    else:
        print('\033[0;31m', end=' ')

    print('{}'.format(c), end=' ')


print('\n\033[mO NUMERO {} FOI DIVIVEL {} VEZES'.format(numero, count))

if count == 2:
    print('POR ISSO É PRIMO')

else:
    print('É POR ISSO QUE ELE NÃO É PRIMO')
