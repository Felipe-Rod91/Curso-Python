velho = 0
idadetotal = 0
mulheres = 0
for pessoas in range(1, 5):
    print('---- {}ª PESSOA ----'.format(pessoas))
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: ').strip())
    sexo = str(input('Sexo (M/F): ').strip())
    idadetotal += idade
    if sexo == 'm':
        if idade > velho:
            velho = idade
            nomehomem = nome
    if sexo == 'f':
        if idade <= 20:
            mulheres += 1
print('A média de idade do grupo é de {:.0f} anos.'.format(idadetotal / pessoas))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, nomehomem))
if mulheres == 1:
    print('Existe {} mulher com menos de 20 anos.'.format(mulheres))
elif mulheres >1:
    print('Existem {} mulheres com menos de 20 anos.'.format(mulheres))
elif mulheres == 0:
    print('Não existe nenhuma mulher com menos de 20 anos.')
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
#do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
