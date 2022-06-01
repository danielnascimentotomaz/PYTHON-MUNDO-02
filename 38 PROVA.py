# Crie um programa que imprima
# todos os quadrados entre n e m. Por exemplo,
# se n for 2 e m for 10, imprimir 4 9 16 25 36 49 64 81 100.


n = int(input('DIGITE VALOR DE N:'))

m = int(input('DIGITE VALOR DE M:'))

for c in range(n, m + 1):
    resultado = c ** 2
    print(resultado, end=' ')
