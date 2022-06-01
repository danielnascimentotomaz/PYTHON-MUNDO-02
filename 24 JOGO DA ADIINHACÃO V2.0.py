"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.

"""

import random

print('\033[32m=-=\033[m' * 20)
print('\033[34mSOU SEU COMPUTADOR.......')
print('ACABEI DE PENSAR EM UM NUMERO ENTRE 0  E 10 ')
print('SERÁ QUE VOCÊ CONSEQUE ADVINHAR QUAL FOI!\033[m')
print('\033[32m=-=\033[m' * 20)

computador = random.randint(0, 10)  # aleatorio
palpite = 0  # contador
acertou = False

while not acertou:
    jogador = int(input('QUAL É SEU PALPITE!'))
    palpite = palpite + 1

    if computador == jogador:
        acertou = True

    else:
        if jogador > computador:
            print('\033[34mMENOS... TENTE MAIS UMA VEZ \033[m')
        elif jogador < computador:
            print('\033[34mMAIS... TENTE MAIS UMA VEZ\033[m')

print('ACERTOU COM {} TENTATIVA.PARABÉNS!'.format(palpite))

"""
from random import randint



computador = randint(0, 10)

print("SOU SEU COMPUTADOR...")
print("SOU SEU COMPUTADOR ACABEI DE PENSAR EM UM NÚMERO ENTRE 0 E 10.")
print("SERÁ QUE VOÇÊ CONSEQUE ADIVINHAR QUAL FOI?")
print(computador)
jogador = int(input("QUAL É SEU PALPITE?"))

count = 0
while computador != jogador:
    count = count + 1

    if jogador > computador:
        print("MENOS... TENTE MAIS UMA VEZ")
    else:
        print("MAIS ... TENTE MAIS UMA VEZ")

    jogador = int(input("QUAL É SEU PALPITE?"))



print('ACERTOU COM {} TENTATIVA.PARABÉNS!'.format(count + 1))

"""