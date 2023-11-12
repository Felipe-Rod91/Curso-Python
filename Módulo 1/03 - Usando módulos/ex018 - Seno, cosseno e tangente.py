# programa que leia um número qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = int(input('Digite o ângulo que você deseja:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'Para o ângulo {ang}, o seu seno é {sen:.3f}, o seu cosseno é {cos:.3f} e sua tangente é {tan:.3f}.')
