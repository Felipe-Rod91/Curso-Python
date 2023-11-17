#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de
#um atleta e mostre sua categoria, de acordo com a idade: até 9 anos: MIRIM; até 14 anos: INFANTIL; até 19 anos: JÚNIOR;
#até 25 anos: SÊNIOR; acima de 25 anos: MASTER.

from datetime import date

ano = int(input('Em que ano o atleta nasceu? '))
idade = date.today().year - ano

print('O atleta tem {} anos.'.format(idade))

if 0 <= idade <= 9:
    print('Ele entra na categoria MIRIM.')
elif 9 < idade <= 14:
    print('Ele entra na categoria INFANTIL.')
elif 14 < idade <= 19:
    print('Ele entra na categoria JÚNIOR.')
elif 19 < idade <= 25:
    print('Ele entra na categoria SÊNIOR.')
elif idade > 25:
    print('Ele entra na categoria MASTER.')
else:
    print('ERRO! ANO INVÁLIDO!')
