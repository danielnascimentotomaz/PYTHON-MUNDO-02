"""
09) Crie um programa que faça o computador jogar Jokenpô com você.
"""

from time import sleep
from random import randint

print('SUAS OPÇOES')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

jogador = float(input('QUAL É SUA JOGADA: '))

print('\033[33mJO\033[m')
sleep(1)
print('\033[34mKEN\033[m')
sleep(1)
print('\033[36mPO!!\033[m')
sleep(1)

# sotear um numero
computador = randint(0, 2)

# LISTA


if jogador in (0, 1, 2):

    itens = ['PEDRA', 'PAPEL', 'TESOURA']

    aleatorio = itens[computador]
    aleatorio11 = itens[int(jogador)]

    print(20 * '=-=')
    print('O COMPUTADOR JOGOU \033[33m{}\033[m'.format(aleatorio))
    print('O JOGADOR JOGOU \033[32m{}\033[m'.format(aleatorio11))
    print(20 * '=-=')

if jogador == 0:

    if computador == 0:
        print('EMPATE')

    elif computador == 1:
        print('COMPUTADOR GANHOU')

    elif computador == 2:
        print('JOGADOR GANHOU')


elif jogador == 1:

    if computador == 0:
        print('JOGADOR GANHOU')

    elif computador == 1:
        print('EMPATE')

    elif computador == 2:
        print('COMPUTADOR GANHOU')


elif jogador == 2:

    if computador == 0:
        print('COMPUTADOR GANHOU')

    elif computador == 1:
        print('JOGADOR VENCEU')

    elif computador == 2:
        print('EMPATE')

else:
    print('\033[0;31mJOGADA INVALIDA......\033[m')
