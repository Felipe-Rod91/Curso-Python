print('=' * 20)
print('BANCO FERFAFE')
print('=' * 20)
saque = int(input('Quanto você deseja sacar? R$'))
total = saque
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        print(f'Total de cédulas de {cedula} reais: {totalcedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
print('VOLTE SEMPRE AO BANCO FERFAFE! TENHA UMA BOA SEMANA!')
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
