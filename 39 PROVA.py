# Escreva um que recebe como parâmetro um inteiro positivo, que representa um determinado ano.
# O programa deve imprime 1 se o ano for bissexto e 0 em caso contrário. Seu programa deve continuar
# pedindo o ano até que digite um número negativo. Um ano é bissexto se ele é divisível por 4.


while True:
    ano = int(input('DIGITE UM ANO'))

    if ano < 0:
        break

    if ano % 4 == 0:
        print('1')

    else:
        print('0')

print('FIM DO PROGRAMA...')
