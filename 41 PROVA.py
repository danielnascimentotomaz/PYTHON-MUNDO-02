# Faça um programa que peça a quantidade de alunos em uma sala,
# peça a idade de cada aluno e imprima a idade média de alunos da sala.


quantidade = int(input('QUAL A QUANTIDADE  DE ALUNO:'))
soma = 0
for c in range(1, quantidade + 1):
    idade = int(input('IDADE:'))
    soma = soma + idade

media = soma / quantidade

print('A MEDIA DE IDADE DA SALA É {}'.format(media))
