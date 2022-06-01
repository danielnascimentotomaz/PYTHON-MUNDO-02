"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa
deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

"""

count = 0
soma = 0
maior = 0
menor = 0


while True:

    valor = float(input("DIGITE UM NÚMERO: "))

    count = count + 1
    soma = soma + valor


    if count == 1:
        maior = valor
        menor = valor
    else:
        if valor < menor:
            menor = valor
        if valor > maior:
            maior = valor

    continuar = ' '
    while continuar not in "SN":
        continuar = str(input("QUER CONTINUAR [S/N]")).upper().strip()[0]

    if continuar == "N":
        break

media = soma / count
print("==========================================")
print("VOÇÊ DIGITOU {} NÚMERO E A MEDIA FOI {:.2f}".format(count, media))
print("O MAIOR VALOR FOI {} E O MENOR VALOR FOI {}".format(maior, menor))


"""
count = 0
soma = 0
maior = 0
menor = 0

siga = False

while not siga:

    valor = float(input("DIGITE UM NÚMERO: "))

    count = count + 1
    soma = soma + valor


    if count == 1:
        maior = valor
        menor = valor
    else:
        if valor < menor:
            menor = valor
        if valor > maior:
            maior = valor

    continuar = ' '
    while continuar not in "SN":
        continuar = str(input("QUER CONTINUAR [S/N]")).upper().strip()[0]

    if continuar == "N":
        siga = True

media = soma / count
print("==========================================")
print("VOÇÊ DIGITOU {} NÚMERO E A MEDIA FOI {:.2f}".format(count, media))
print("O MAIOR VALOR FOI {} E O MENOR VALOR FOI {}".format(maior, menor))

"""


"""
count = 0
soma = 0
maior = 0
menor = 0

continuar = "S"

while continuar in "Ss":

    valor = float(input("DIGITE UM NÚMERO: "))

    count = count + 1
    soma = soma + valor


    if count == 1:
        maior = valor
        menor = valor
    else:
        if valor < menor:
            menor = valor
        if valor > maior:
            maior = valor


    continuar = str(input("QUER CONTINUAR [S/N]")).upper().strip()[0]



media = soma / count
print("==========================================")
print("VOÇÊ DIGITOU {} NÚMERO E A MEDIA FOI {:.2f}".format(count, media))
print("O MAIOR VALOR FOI {} E O MENOR VALOR FOI {}".format(maior, menor))

"""