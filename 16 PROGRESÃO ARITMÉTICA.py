"""16) Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão. """

print('^=' * 30)
print('{:^40}'.format('\033[0;32m10 TERMOS DE UMA PA\033[m'))
print('^=' * 30)

termos = int(input('PRIMEIRO  TERMO: '))
razao = int(input('RAZÃO: '))

decimo = termos + (10 - 1) * razao # Fórmula do Termo Geral

for c in range(termos, decimo + 1, razao):
    print(c, end=' → ')
print("ACABOU")
