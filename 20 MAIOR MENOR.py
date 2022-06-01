"""20) Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""
menor = 0
maior = 0

for c in range(1, 6):
    peso = float(input('PESO DA {}º PESSOA:'.format(c)))

    if c == 1:
        menor = peso
        maior = peso

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O MAIOR PESO LIDO FOI DE {}KG'.format(maior))
print('O MENOR PESO LIDO FOI DE {}KG'.format(menor))