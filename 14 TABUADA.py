"""
14)mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

"""

valor = int((input('DIGITE UM VALOR PRA VER SUA TABUADA:')))
for c in range(0, 11):
    print('{:2} X {} = {}'.format(c, valor, valor * c))
