# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.


contar = 0
contar2 = 0
contar3 = 0

while True:

    print('-=-' * 20)
    print('\033[32m             CADRASTE UMA PESSOA\033[m')
    print('-=-' * 20)

    idade = int(input('IDADE:'))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO:[M/F]')).upper().strip()[0]

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('QUER CONTINAR [S/N]')).strip().upper()[0]

    if idade > 18:  # contagen de idade
        contar = contar + 1

    if sexo == 'M':  # CONTAGEM DE SE HOMEM
        contar2 = contar2 + 1

    if sexo == 'F':  # conta quantidade de mulheres com menos de 20 anos
        if idade < 20:
            contar3 = contar3 + 1

    if continuar == 'N':
        break
print(">>>" * 15)
print('TOTAL DE PESSOAS COM MAIS DE 18 ANOS FOI : {}'.format(contar))
print('AO TODO TEMOS {} HOMEM CADRASTADOS '.format(contar2))
print('E TEMOS {} MULHERES COM MENOS DE 20 ANOS '.format(contar3))
