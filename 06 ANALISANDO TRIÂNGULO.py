"""
06), acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

"""

primeiro = float(input('PRIMEIRO SEGMENTO:'))
segundo = float(input('SEGUNDO SEGMENTO:'))
terceiro = float(input('TERCEIRO SEGMENTO:'))

if primeiro < (segundo + terceiro) and segundo < (primeiro + terceiro) and terceiro < (primeiro + segundo):

    print('OS SEGMENTO ACIMA PODEM FORMA UM TRIÂNGULO ', end='')

    if primeiro == segundo == terceiro:
        print('EQUILÁTERO!')


    elif primeiro != segundo and primeiro != terceiro and terceiro != segundo:
        print('ESCALENO!')

    else:
        print('ISÓSCELES!')


else:
    print('OS SEGMENTO ACIMA NÃO PODE FORMAR UM TRIÂNGULO')



"""
a = float(input("PRIMEIRO SEGMENTO: "))
b = float(input("SEGUNDO SEGMENTO: "))
c = float(input("TERCEIRO SEGMENTO: "))
maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

if (a + b + c - maior) > maior:
    print("OS SEGMENTO ACIMA PODEM FORMAR UM TRIÂNGULO ", end= '')

    if a == b and b == c:
        print("equilatero")

    elif a != b and a != c and c != b:
        print("ESCALENO")

    else:
        print("ISÓSCELES")
else:
    print("OS SEGMENTO NÃO PODE FORMA UM TRIÂNGULO")


"""