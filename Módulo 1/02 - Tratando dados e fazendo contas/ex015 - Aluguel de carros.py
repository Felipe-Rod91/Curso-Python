# programa para calcular qual o aluguel de um carro, sendo 60 reais o preço por dia alugado e 15 centavos por quilômetro
# rodado com ele

dias = int(input('Por quantos dias o carro ficou alugado? '))
km = int(input('Quantos km foram rodados com o carro? '))
print(f'Se o carro foi alugado por {dias} dias e rodou {km}km, então o valor do aluguel é igual a '
      f'{(dias * 60) + (km * 0.15):.2f} reais.')
