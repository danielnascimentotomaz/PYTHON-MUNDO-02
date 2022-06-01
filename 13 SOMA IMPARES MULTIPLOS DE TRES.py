"""
13)Faça um programa que calcule a soma entre todos os números impares que são múltiplos
de três e que se encontram no intervalo de 1 até 500.


"""

soma = 0
count = 0
for c in range(0, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c
        count = count + 1
print('A SOMA TODOS OS {} VALORES SOLICITADO É {}'.format(count, soma))
