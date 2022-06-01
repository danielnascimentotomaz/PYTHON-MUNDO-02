"""
04) Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
 de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO

"""

n1 = float(input("PEIMEIRA NOTA: "))
n2 = float(input("SEGUNDA NOTA: "))

media = (n1 + n2) / 2

print("TIRANDO {:.1f} E {:.1f}, A MÉDIA É {:.1f}".format(n1, n2, media))

if media < 5:
    print("O ALUNO ESTÁ REPROVADO")
elif 5 <= media < 7:
    print("O ALUNO ESTÁ EM RECUPERAÇÃO")
else:
    print("O ALUNO ESTÁ APROVADO")