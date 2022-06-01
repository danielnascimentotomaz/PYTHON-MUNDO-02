# Faça um programa que peça ao usuário a quantidade de termos da série calcule
# o valor da série: S = 3/2 + 6/4 + 9/6 +12/8 + ...+ n*3/n*2


serie = int(input('QUANTIDADE DE TERMO DA SERIE'))

print('S = ', end='')

for c in range(1, serie + 1):
    print('{}/{}'.format(c * 3, c * 2), end=' + ')
