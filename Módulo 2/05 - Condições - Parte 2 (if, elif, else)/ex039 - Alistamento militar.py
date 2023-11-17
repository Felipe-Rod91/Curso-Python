#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
#alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
#também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano

print('O rapaz tem, atualmente, {} anos.'.format(idade))

if idade > 18:
    print(f'O candidato já passou do tempo do alistamento em {idade - 18} ano(s).')
elif idade < 18:
    print(f'O candidato ainda não chegou na idade para o alistamento. Falta(m) {18 - idade} ano(s) para tal.')
elif idade == 18:
    print(f'O candidato está na idade exata para se alistar, procure o posto de recrutamento mais próximo.')
