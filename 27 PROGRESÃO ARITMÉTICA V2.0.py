"lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."

print('GERADOR DE PA')
print('=-=' * 10)

primeiro = int(input('PRIMEIRO TERMO:'))
razao = int(input('RAZÃO:'))

termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' ')
    if cont < 10:
        print('<>',end=' ')
    else:
        print('...', end=' ')

    termo = termo + razao
    cont = cont + 1
print('FIM')
