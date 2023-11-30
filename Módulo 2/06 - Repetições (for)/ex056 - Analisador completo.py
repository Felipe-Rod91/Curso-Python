#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
#do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

velho = 0
idadetotal = 0
mulheres = 0
for pessoas in range(1, 5):
    print(f'---- {pessoas}ª PESSOA ----')
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
print(f'A média de idade do grupo é de {idadetotal / pessoas:.0f} anos.')
print(f'O homem mais velho tem {velho} anos e se chama {nomehomem}.')

if mulheres == 1:
    print(f'Existe {mulheres} mulher com menos de 20 anos.')
elif mulheres > 1:
    print(f'Existem {mulheres} mulheres com menos de 20 anos.')
elif mulheres == 0:
    print('Não existe nenhuma mulher com menos de 20 anos.')
