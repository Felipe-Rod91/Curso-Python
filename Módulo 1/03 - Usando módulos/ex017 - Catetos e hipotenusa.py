# programa que calcula o comprimento da hipotenusa quando informados os comprimentos dos catetos.

import math

co = int(input('Digite o cateto oposto do triângulo: '))
ca = int(input('Digite o cateto adjacente do triângulo: '))
hip = math.sqrt((co ** 2) + (ca ** 2))
print(f'A hipotenusa do triângulo retângulo é de {hip:.2f}.')
