# 21)Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de
# idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma = 0  # ACUMULADOR
media = 0
homemmaisvelho = ''
count = 0  # CONTADOR
count1 = 0  # CONTADOR
maior = 0

for c in range(1, 5):
    print('===== {}° PESSOA ======='.format(c))
    nome = str(input('NOME:')).strip().upper()
    idade = int(input('IDADE:'))
    sexo = str(input('[M/F]:')).strip().upper()

    soma = soma + idade  # acumuladador
    media = soma / c  # media da idade

    # MAIOR IDADE
    if sexo == 'M':
        if c == 1:
            maior = idade
            homemmaisvelho = nome
        else:
            if idade > maior:
                maior = idade
                homemmaisvelho = nome

    # QUANTIDADE DE MULHERES COM MENOS DE 20 ANOS
    if sexo == 'F':
        if idade < 20:
            count1 = count1 + 1

print('A MEDIA DE IDADE DO GRUPO É DE {:.2f} ANOS'.format(media))
print('O HOMEM MAIS VELHO TEM {} ANOS E SE CHAMA {} '.format(maior, homemmaisvelho))
print('AO TODO SÃO {} MULHERES  COM MENOS DE 20 ANOS'.format(count1))
