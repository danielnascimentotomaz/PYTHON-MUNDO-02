"""
02)Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

"""

num1 = float(input('DIGITE PRIMEIRO NUMERO:'))

num2 = float(input('DIGITE SEGUNDO NUMERO:'))

if num1 > num2:
    print('O PRIMERIO NUMERO É MAIOR')

elif num2 > num1:
    print('O SEGUNDO NUMERO É MAIOR ')

else:
    print('OS DOIS VALORES SÃO IGUAIS')