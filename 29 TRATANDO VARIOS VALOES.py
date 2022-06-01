"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre eles (desconsiderando o flag).
"""


cont = 0
soma = 0
num = 0
while num != 999:
    num = int(input('DIGITE UM NUMERO [999 PARA PARAR]: '))
    if num != 999:
        cont = cont + 1
        soma = soma + num



print('VOCÊ DIGITOU {} NUMEROS E A SOMA ENTRE ELES FOI {}'.format(cont, soma))