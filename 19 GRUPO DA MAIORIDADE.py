""" 19)Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
   não atingiram a maioridade e quantas já são maiores."""

from datetime import date

atual = date.today().year
count = 0
count1 = 0
for c in range(1, 8):
    anonascimento = int(input('EM QUE ANO {}° PESSOA NASCEU!'.format(c)))
    idade = atual - anonascimento

    if idade >= 21:
        count = count + 1
    else:
        count1 = count1 + 1

print('AO  TODO TIVEMOS {} PESSOAS MAIORES  DE IDADE '.format(count))
print('E TAMBÉM TIVEMOS {} PESSOAS MENORES DE IDADE '.format(count1))
