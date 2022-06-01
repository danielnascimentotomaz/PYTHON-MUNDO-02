"""
01) Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
 1 para binário, 2 para octal e 3 para hexadecimal.
"""

n = int(input("DIGITE UM NÚMERO INTEIRO: "))
print("==================================================")
print("""----------------------------------
ESCOLHA UMA DAS BASES DE CONVERSÃO:
-----------------------------------
[1] CONVERTER PARA BINÁRIO 
[2] CONVERTER PARA OCTAL
[3] CONVERTER PARA HEXADECIMAL
[4] SAI DO PROGRAMA """)
print("==================================================")

x = int(input("QUAL SUA OPÇÃO: "))
while x > 4 or x < 1:
    print("OPÇÃO INVALIDA DIGITE NOVAMENTE.")
    x = int(input("QUAL SUA OPÇÃO: "))

if x == 1:
    print("{} CONVERTIDO PARA BINÁRIO É IQUAL A  {} ".format(n, bin(n)[2:]))

elif x == 2:
    print("{} CONVERTIDO PARA OCTAL É IGUAL A {} ".format(n, oct(n)[2:]))

elif x == 3:
    print("{} CONVERTIDO PARA HEXADECIMAL É IQUAL A {} ".format(n, hex(n[2:])))

print("FIM DO PROGRAMA.")