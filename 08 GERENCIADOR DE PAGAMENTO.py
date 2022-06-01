"""
08)Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço normal

– 3x ou mais no cartão: 20% de juros

"""





print(f'{" CASAS BANHIA ":=^40}')

preco = float(input('PREÇO DAS COMPRAS: R$'))

print('FORMA DE PAGAMENTO')

print('[ 1 ] Á VISTA DINHEIRO / CHEQUE')
print('[ 2 ] Á VISTA CARTÃO')

print('[ 3 ] 2X CARTÃO ')
print('[ 4 ] 3x OU MAIS NO CARTÃO')

opcao = int(input('QUAL É OPÇÃO?'))

###### PORCENTAGEN#######
# 10 POR CENTO
desconto = (preco * 10) / 100

# 5 por cento
desconto1 = (preco * 5) / 100

# 20 por cento
aumento2 = (preco * 20) / 100


if opcao == 1:
    total = preco - desconto

elif opcao == 2:
    total = preco - desconto1

elif opcao == 3:
    total = preco
    valor0 = preco / 2
    print('SUA COMPRA SERÁ PARCELADA EM 2x DE R${:.2f} SEM JUROS '.format(valor0))


elif opcao == 4:
    parcelas1 = int(input('QUANTAS PARCELAS'))
    valor = (preco + aumento2) / parcelas1
    total = preco + aumento2
    print('SUA COMPRA SERÁ PARCELADA EM {}X DE R$ {:.2f} COM JUROS'.format(parcelas1, valor))

else:
    total = 0
    print('\033[31mOPÇÃO INVALIDA\033[m')

print('SUA COMPRA DE R${:.2f} VAI CUSTAR R${:.2f} NO FINAL'.format(preco, total))