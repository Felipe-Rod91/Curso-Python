#programa que converte a temperatura em Celsius para Kelvin e Farenheit

temp = float(input('Qual a temperatura em graus Celsius?'))
print(f'Se a temperatura é de {temp}ºC, então é é de {temp + 273:.1f}K em Kelvin e {(temp * 1.8) + 32:.1f}F '
      f'em Farenheit.')
