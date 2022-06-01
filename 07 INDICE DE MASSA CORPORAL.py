"""
07)Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida

"""


peso = float(input('QUAL É SEU PESO ? (KG)'))

altura = float(input('QUAL É SUA ALTURA? (M)'))

imc = peso / (altura**2)
print('O IMC DESSA PESSOA É DE {:.1f}'.format(imc))

if imc < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO NORMAL')

elif 18.5 <= imc < 25:
    print('PARABÊM , VOÇÊ ESTÁ NA FAIXA DO PESO NORMAL')

elif 25 <= imc < 30:
    print('VOCÊ ESTA EM SOBREPESO')

elif 30 <= imc < 40:
    print('VOÇÊ ESTA EM OBESIDADE')

else:
    print('VOÇÊ EM OBESIDADE MÓRBIDA, CUIDADO!')