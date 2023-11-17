#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
#a média atingida: média abaixo de 5.0: REPROVADO; média entre 5.0 e 6.9: RECUPERAÇÃO; média 7.0 ou superior: APROVADO

n1 = float(input('Qual a nota do primeiro semestre? '))
n2 = float(input('Qual a nota do segundo semestre? '))
media = (n1 + n2) / 2

print('A sua média é {}.'.format(media))

if media < 5:
    print('Sinto muito, você foi REPROVADO!')
elif media >= 7:
    print('Parabéns, você foi APROVADO!')
elif 5 <= media < 7:
    print('Você está de RECUPERAÇÃO.')
