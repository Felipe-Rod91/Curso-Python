# programa que transforma um número flutuante em inteiro

import math

numint = float(input('Digite um número com vírgula: '))
numintint = math.trunc(numint)
print(f'O número {numint} sem as vírgulas é {numintint}.')
