"""
05)A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
 de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""

from datetime import date

anoatual = date.today().year

ano = int(input("ANO DE NASCIMENTO: "))

idade = anoatual - ano

print("O ATLETA TEM {} ANOS".format(idade))
if idade <= 9:
    print("CLASSIFICAÇÃO : MIRIM")

elif 9 < idade <= 14:
    print("CLASSIFICAÇÃO : INFANTIL")

elif 14 < idade <= 19:
    print("CLASSIFICAÇÃO: JÚNIOR")

elif 19 < idade <= 25:
    print("CLASSIFICAÇÃO: SÊNIOR")
else:
    print("CLASSIFICAÇÃO: MASTER")
