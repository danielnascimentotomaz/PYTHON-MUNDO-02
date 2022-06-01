"""
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

"""









from time import sleep
primeiro = int(input('PRIMEIRO VALOR:'))
segundo = int(input('SEGUNDO VALOR:'))

opcao = 0
while opcao != 5:
    print('     [1] SOMAR')
    print('     [2] MULTIPLICAR')
    print('     [3] MAIOR')
    print('     [4] NOVOS NUMEROS')
    print('     [5] SAIR DO PROGRAMA')
    opcao = int(input('>>>> QUAL É SUA OPÇÃO'))
    print('processando....')
    sleep(1)
    # SOMA
    if opcao == 1:
        somar = primeiro + segundo
        print('A SOMA ENTRE {} + {} É {}'.format(primeiro, segundo, somar))

    # MULTIPPLICAÇÃO
    elif opcao == 2:
        multiplicar = primeiro * segundo
        print('A MULTIPLICAÇÃO ENTRE {} * {} É {}'.format(primeiro, segundo, multiplicar))

    # MAIOR
    elif opcao == 3:
        if primeiro == segundo:
            print('NÃO EXISTE MAIOR OS VALORES SÃO IGUAIS A {}'.format(primeiro))

        elif primeiro > segundo:
            print('ENTRE {} E {} MAIOR VALOR É {}'.format(primeiro, segundo, primeiro))

        elif segundo > primeiro:

            print('ENTRE {} E {} MAIOR VALOR É {}'.format(primeiro, segundo, segundo))

    elif opcao == 4:
        print('INFORME NOVO VALOR ')
        primeiro = int(input('PRIMEIRO VALOR:'))
        segundo = int(input('SEGUNDO VALOR:'))


    # opcão invalida
    elif opcao > 5:
        print('OPÇÃO INVALIDA ! TENTE NOVAMENTE')



    print('-=-' * 10)

print('FIM DO PROGRAMA! VOLTE SEMPRE')



"""
from time import sleep
primeiro = int(input('PRIMEIRO VALOR:'))
segundo = int(input('SEGUNDO VALOR:'))

final = False
while  not final:
    print('     [1] SOMAR')
    print('     [2] MULTIPLICAR')
    print('     [3] MAIOR')
    print('     [4] NOVOS NUMEROS')
    print('     [5] SAIR DO PROGRAMA')
    opcao = int(input('>>>> QUAL É SUA OPÇÃO'))
    print('processando....')
    sleep(1)
    # SOMA
    if opcao == 1:
        somar = primeiro + segundo
        print('A SOMA ENTRE {} + {} É {}'.format(primeiro, segundo, somar))

    # MULTIPPLICAÇÃO
    elif opcao == 2:
        multiplicar = primeiro * segundo
        print('A MULTIPLICAÇÃO ENTRE {} * {} É {}'.format(primeiro, segundo, multiplicar))

    # MAIOR
    elif opcao == 3:
        if primeiro == segundo:
            print('NÃO EXISTE MAIOR OS VALORES SÃO IGUAIS A {}'.format(primeiro))

        elif primeiro > segundo:
            print('ENTRE {} E {} MAIOR VALOR É {}'.format(primeiro, segundo, primeiro))

        elif segundo > primeiro:

            print('ENTRE {} E {} MAIOR VALOR É {}'.format(primeiro, segundo, segundo))

    elif opcao == 4:
        print('INFORME NOVO VALOR ')
        primeiro = int(input('PRIMEIRO VALOR:'))
        segundo = int(input('SEGUNDO VALOR:'))


    # opcão invalida
    elif opcao > 5 or opcao < 1 :
        print('OPÇÃO INVALIDA ! TENTE NOVAMENTE')

    elif opcao == 5:
        final = True




    print('-=-' * 10)

print('FIM DO PROGRAMA! VOLTE SEMPRE')






"""
