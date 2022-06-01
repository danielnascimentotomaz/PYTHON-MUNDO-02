"""
38) Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

Aula Anterior
Voltar para Módulo
ATENÇÃO: O botão de concluir aula só fica clicável depois que toda a aula é assistida

Para avançar no andamento dos cur
"""

nome = str(input("DIGITE SEU NOME:")).upper().strip()

l = nome.split()

junta = ''.join(l)

inverso = ''
for letra in range(len(junta) - 1, -1, -1):
    inverso = inverso + junta[letra]

if inverso == nome:
    print("TEMOS UM PALINDROMO:")
else:
    print("A FRASE DIGITADA NÃO PODE FORMA UM PALINDROMO")





"""
nome = str(input("digite um nome"))
a = nome.split()

l = ''.join(a)

junta = []
for j in range(len(l) - 1, -1, -1):
    junta.append(l[j])

h = ''.join(junta)


if nome == h:
    print("TEMOS UM PALINDROMO:")
else:
    print("A FRASE DIGITADA NÃO PODE FORMA UM PALINDROMO")









"""