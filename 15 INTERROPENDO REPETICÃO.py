soma = 0

while True:
    n = int(input('digite um valor:'))
    if n == 4:
        break
    soma = soma + n

# print('A SOMA DE TODOS VALORES É {}'.format(soma))
print(f'A SOMA DE TODOS OS VALORES FOI {soma:.2f}')  # novo modelo de print
print('FIM')

# ex : de novo print

nome = 'maria'
idade = 12
print(f'{nome} tem {idade} anos')
