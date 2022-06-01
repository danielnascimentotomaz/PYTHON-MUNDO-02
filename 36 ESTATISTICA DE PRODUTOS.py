"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""

print('-=-' * 20)
print('           LOJA SUPER BARATÃO ')
print('-=-' * 20)

total = 0
contar = 0
menor = 0
contar1 = 0
barato = ''

while True:

    produto = str(input('NOME DO PRODUTO = '))

    preco = float(input('PREÇO: R$'))

    contar1 = contar1 + 1  # contador

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('QUER CONTINUAR![S/N]')).strip().upper()[0]

    total = total + preco  # valor total da compras

    if preco > 1000:  # produto acima de 1000 reais
        contar = contar + 1

    # MENOR PREÇO
    if contar1 == 1:
        menor = preco
        barato = produto  # nome do produto

    else:
        if preco < menor:
            menor = preco
            barato = produto

    if continuar == 'N':
        break
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("{:^40}".format('FIM DO PROGRAMA'))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

print('O TOTAL DA COMPRA FOI R${:.2f}'.format(total))

print('TEMOS {} PRODUTO CUSTANTO MAIS DE R$ 1000.00'.format(contar))

print('O PRODUTO MAIS BARATO FOI {} QUE CUSTA R$ {:.2f}'.format(barato, menor))
