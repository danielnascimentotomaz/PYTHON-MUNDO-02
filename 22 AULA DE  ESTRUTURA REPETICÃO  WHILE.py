
# USAR WHILE  QUANDO NÃO CONHECO  O INTERVALO
# WIHILE = EQUUANTO


"""s = 0  # contador
while s < 10:
    s = s + 1
    print(s, end=' ')"""

"""# contagem regressia
s = 11
while s > 1:
    s = s - 1
    print(s)"""

"""# 2) enquanto o numero for diferente de 0 fica lendo
n = 1
while n != 0:
    n = int(input('digite um valor'))
print('fim')"""

"""resposta = 'S'
cout = 0
while resposta == 'S':
    n = int(input('digite valor'))
    resposta = str(input('QUER CONTINUAR[S/N]')).upper()
    cout = cout + n
print('TOTAL {}'.format(cout))
print('FIM')"""

# ANALISANDO

n = 1
count1 = 0
count2 = 0
while n != 0:
    n = int(input('DIGITE UM VALOR'))
    if n != 0:
        if n % 2 == 0:
            count1 = count1 + 1
        else:
            count2 = count2 + 1

print('O TOTAL DE NUMEROS PARES DIGITADO FOI {}'.format(count1))
print('O TOTAL DE NUMERO IMPAR DIGITADO FOI {}'.format(count2))




