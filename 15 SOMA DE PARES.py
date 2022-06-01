"""
14)Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.

"""

s = 0
count = 0
for c in range(1, 7):
    valor = int(input('DIGITE UM VALOR:'))

    if valor % 2 == 0:
        s = s + valor
        count = count + 1

print('VOCÊ INFORMOU {} NUMEROS PARES E SOMA FOI {}'.format(count, s))
