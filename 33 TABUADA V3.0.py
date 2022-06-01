"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para
cada valor digitado pelo usuário. O programa será interrompido quando o número
solicitado for negativo.

"""


while True:
    valor = int(input('QUER VER A TABUADA DE QUAL VALOR: '))

    if valor < 0:
        break
    print('-=-' * 13)
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(valor, c, c * valor))

    print('=-=' * 20)
print('-=-' * 20)
print('PROGRAMA TABUADA ENCERRRADO VOLTE SEMPRE!!!')
