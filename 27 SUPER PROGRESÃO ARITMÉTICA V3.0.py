"""
perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

"""


print("==============")
print("GERADOR DE PA:")
print("==============")

termo = int(input("PRIMEIRO TERMO: "))
razao = int(input("RAZÃO DA PA: "))

contar = 0
total = 1
mais = 0
y = 10

continuar = False

while not continuar:
    y = y + mais
    while total <= y:
        print("{}".format(termo), end='')
        if total < 10:
            print(" => ", end='')
        else:
            print("=>", end=" ")

        termo = termo + razao
        total = total + 1
        contar = contar + 1

    print("pause")

    mais = int(input("QUANTOS TERMOS DESEJA SOMA A MAIS: "))
    if mais == 0:
        continuar = True
print("PROGREÇÃO FOI FINALIZADA COM {} TERMOS MOSTRADO".format(contar))



















"""print('GERADOR DE PA')
print('-=-' * 20)

termo = int(input('PRIMEIRO TERMO:'))
razao = int(input('RAZÃO DA PA:'))

c = 1
mais = 10
total = 0


while mais != 0:
    total = mais + total
    while c <= total:
        print('{}'.format(termo), end=' ')
        print('<>' if c < 10 else '', end=' ')
        termo = termo + razao
        c = c + 1
        contar = total + 1
    print('PAUSA ')
    mais = int(input('QUANTOS TERMOS VOCÊ QUER MOSTRAR A MAIS'))

print('PROGRESSÃO FINALIZADA COM {} TERMOS MOSTRADO'.format(total))"""

"""
1 => EXERCICIO POTÊNCIA DE 2:

while True:
    y = y + mais
    while total <= y:
        print(2 **a)

        total = total + 1
        a = a + 1

    mais = int(input("DESEDJA SOMA QUANTOS NÚMERO A MAIS: "))

    if mais == 0:
        break






"""