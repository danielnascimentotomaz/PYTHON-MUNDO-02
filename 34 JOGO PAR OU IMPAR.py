
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print("===========================")
print("VAMOS JOGAR PAR OU IMPAR")
print("===========================")

count = 0
while True:
    jogador = int(input("DIGA UM VALOR: "))

    TIPO = ' '
    while TIPO not in "PI":
        TIPO = str(input("PAR OU IMPAR [P/I]: ")).strip().upper()[0]

    computador = randint(0, 11)
    total = computador + jogador

    print("===============================")
    print("VOÇÊ JOGOU {} E O COMPUTADOR {}. TOTAL DEU {} ".format(jogador, computador, total), end='')
    if total % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")

    if TIPO == "P":

        print("=========================")
        if total % 2 == 0:
            print("VOÇÊ VENCEU")
            count = count + 1
        else:

            print("VOÇÊ PERDEU")
            break

    elif TIPO == "I":
        print("=========================")
        if total % 2 != 0:
            print("VOÇÊ VENCEU")
            count = count + 1
        else:
            print("\033[31mVOÇÊ PERDEU\033[m")
            break

    print("VAMOS JOGAR NOVAMENTE....")
print("=========================")
print("\033[35mGAMER OVER! VOÇÊ VENCEU\033[m {} \033[35mVEZES\033[m".format(count))

