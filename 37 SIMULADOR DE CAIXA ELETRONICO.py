# Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
# pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


"""print('=-=' * 20)
print('{:^50}'.format('BANCO CEV'))
print('-=-' * 20)

nt50 = 0
nt20 = 0
nt10 = 0
nt1 = 0

valor = int(input('QUE VALOR VOCÊ QUER SACAR R$:'))

# nota de 50
for a in range(1, valor + 1):

    if a % 50 == 0:
        nt50 = nt50 + 1
resto1 = valor - (50 * nt50)  # RESTO

# nota de 20
for b in range(1, resto1 + 1):
    if b % 20 == 0:
        nt20 = nt20 + 1
resto2 = resto1 - (20 * nt20)  # RESTO

# nota de 10
for c in range(1, resto2 + 1):
    if c % 10 == 0:
        nt10 = nt10 + 1
resto3 = resto2 - (nt10 * 10)  # RESTO

# nota de 1
for c in range(1, resto3 + 1):
    nt1 = nt1 + 1

print('TOTAL DE {} CÉDULA DE R$ 50'.format(nt50))
print('TOTAL DE {} CÉDULA DE R$ 20'.format(nt20))
print('TOTAL DE {} CÉDULA DE R$ 10'.format(nt10))
print('TOTAL DE {} CÉDULA DE R$ 1'.format(nt1))"""

# USANDO WHILE
print('==' * 30)
print('{: ^60}'.format('BANCO CEV'))
print('==' * 30)

valor = int(input('QUE VALOR VOÇÊ QUER SACAR R$:'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total = total - ced
        totalced = totalced + 1
    else:

        if totalced > 0:
            print(f'TOTAL DE {totalced} CÉDULA DE R$ {ced} ')

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0

        if total == 0:
            break
print('==' * 30)
print('VOLTE SEMPRE AO BANCO CEV')
"""
valor = float(input('QUE VALOR VOÇÊ QUER SACAR R$:'))


totalced = 0
totalced20 = 0
totalced10 = 0
totalced5 = 0
totalced1 = 0

while valor > 0:
    if valor >= 50:
        valor = valor - 50
        totalced = totalced + 1
    else:
        if valor >= 20:
            totalced20 = totalced20 + 1
            valor = valor - 20
        elif valor >= 10:
            valor = valor - 10
            totalced10 = totalced10 + 1
        elif valor >= 5:
            valor = valor - 5
            totalced5 = totalced5 + 1
        elif valor >= 1:
            valor = valor - 1
            totalced1 = totalced1 + 1
        else:
            break

print(f"TOTAL DE CELULAS DE R$: 50 É {totalced}")
print(f"TOTAL DE CELULAS DE R$: 20 É {totalced20}")
print(f"TOTAL DE CELULAS DE R$: 10 É {totalced10}")
print(f"TOTAL DE CELULAS DE R$: 5 É {totalced5}")
print(f"TOTAL DE CELULAS DE R$: 1 É {totalced1}")

"""