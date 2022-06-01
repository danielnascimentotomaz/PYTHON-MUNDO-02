"""
00)Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

"""



valor = float(input("VALOR DA CASA: R$"))
salario = float(input("SALÁRIO DO COMPRADOR: R$"))
parcelas = int(input("QUANTOS ANOS DE FINANCIAMENTO?"))

pretacao = valor / (parcelas * 12)
 
porcentagemdosalario = (salario * 30) / 100



print("PARA PAGAR UMA CASA DE R${:.2f} EM {} ANOS A PRESTAÇÃO SERÁ DE R${:.2f} POR MÊS".format(valor, parcelas, pretacao))

if pretacao <= porcentagemdosalario:
    print("EMPRÉSTIMO PODE SER CONCEDIDO")
else:
    print("EMPRÉSTIMO NEGADO!")

