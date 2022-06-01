"""
 Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8

"""
print('-' * 50)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 50)

a = int(input('QUANTO TERMOS VOCÊ QUER MOSTRAR!'))
print('~' * 40)

x = 1 #CONTADOR
c = 0
z = 0
j = 1

print("{} =>".format(z), end=' ')

while x <= a - 1:
    c = j + z
    print(c, end=' ')


    if x < a - 1:
        print("=>",end=" ")

    else:
        print("-> FIM")

    x = x + 1

    z = c
    j = c - j









"""print('-' * 50)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 50)

n = int(input('QUANTO TERMOS VOCÊ QUER MOSTRAR!'))
print('~' * 40)

t1 = 0

t2 = 1

c = 3

print('{} {}'.format(t1, t2), end=' ')

while c <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('{}'.format(t3), end=' ')
    c = c + 1

print('FIM')"""
