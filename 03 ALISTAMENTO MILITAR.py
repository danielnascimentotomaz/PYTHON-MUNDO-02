"""
03)Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
 se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""

from datetime import date

nascimento = int(input('DATA DE NASCIMENTO:'))

print(20*'=-=')

print('             SEXO          ')
print('HOMEM = H')
print('MULHER = M')

print(20*'=-=')

sexo = str(input('QUAL SEU SEXO:')).upper()



# calculo do ano atual

anoatual = date.today().year

# calculo da idade
idade = anoatual - nascimento

# ano do alistamento:
ano = nascimento + 18

if sexo == 'M':
    print('VOCÊ NAO PRECISSAR ALISTA ')

if sexo == 'H':
    print('QUEM NASCEU EM {} TEM {} ANOS EM {} '.format(nascimento, idade, anoatual))

    if idade == 18:
        print('VOCÊ TEM QUE SE ALISTAR IMEDIATAMENTE')

    elif idade < 18:
        falta = 18 - idade
        print('AINDA FALTA {} ANOS PARA O ALISTAMENTO '.format(falta))
        print('SEU ALISTAMENTO SERÁ EM {}'.format(ano))

    elif idade > 18:
        passou = idade - 18
        print('VOCÊ JA DEVERIA TER SE ALISTADO HÁ {} ANOS'.format(passou))
        print('SEU ALISTAMENTO FOI EM {}'.format(ano))
