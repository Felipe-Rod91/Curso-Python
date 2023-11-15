# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Qual a velocidade do carro em km/h? '))
print('Calculando...')

if vel > 80:
    print(f'Você ultrapassou a velocidade máxima permitida em {vel - 80}km/h.')
    print(f'Sua multa é de {(vel - 80) * 7:.2f} reais')
else:
    print('Você estava dentro do limite de velocidade permitido. Boa viagem!')
