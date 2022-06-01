"""
23)Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
peça a digitação novamente até ter um valor correto

"""


sexo = str(input('INFORME SEU SEXO[M//F]')).upper().strip()[0]

while sexo != 'M' and sexo != 'F':
    sexo = str(input('DADOS INVALIDO .POR FAVOR , INFORME  SEU SEXO: ')).upper().strip()[0]

print('SEXO {} REGISTRADO COM SUCESSO'.format(sexo))


"""
sexo = str(input("INFORME SEU SEXO: ")).strip().upper()[0]

while sexo not in "MF":
    sexo = str(input("DADOS INVALIDOS. POR FAVOR, INFORME SEU SEXO:")).strip().upper()[0]
print("SEXO {} REGISTRADO COM SUCESSO.".format(sexo))


"""