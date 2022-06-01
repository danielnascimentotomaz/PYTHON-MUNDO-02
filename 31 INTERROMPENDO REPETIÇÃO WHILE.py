"""
vamos aprender como utilizar a instrução break e os loopings infinitos a favor
das nossas estratégias de código. É muito importante saber usar o break no Python,
já que em alguns casos precisamos interromper um laço no meio do caminho.

"""

# EX1

count = 1
while True:
    valor = int(input("DIGITE UM VALOR:"))
    count = count + 1
    if count == 10:
        break

