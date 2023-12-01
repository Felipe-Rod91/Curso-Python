# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos;
# B) quantos homens foram cadastrados;
# C) quantas mulheres tem menos de 20 anos.

dezoito = homens = mulheres20 = 0
while True:
    sexo = continuar = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [ M / F ]: ').strip().upper())
    if sexo == 'M':
        homens += 1
    idade = int(input('Idade: ').strip())
    if idade >= 18:
        dezoito += 1
    if idade <= 20 and sexo == 'F':
        mulheres20 += 1
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [ S / N ] ').upper().strip())
    if continuar == 'S':
        print('-' * 20)
    elif continuar == 'N':
        break
print(f'''Finalizando...
Foram cadastradas {dezoito} pessoas com mais de 18 anos.
Foram cadastrados {homens} homens.
Foram cadastradas {mulheres20} mulheres com menos de 20 anos.''')
