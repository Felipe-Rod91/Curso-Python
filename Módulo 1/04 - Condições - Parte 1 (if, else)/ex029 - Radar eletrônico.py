vel = int(input('Qual a velocidade do carro em km/h? '))
print('Calculando...')
if vel > 80:
    print('Você ultrapassou a velocidade máxima permitida em {}km/h.'.format(vel - 80))
    print('Sua multa é de {:.2f} reais'.format((vel - 80) * 7))
else:
    print('Você estava dentro do limite de velocidade permitido. Boa viagem!')
#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
#foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
