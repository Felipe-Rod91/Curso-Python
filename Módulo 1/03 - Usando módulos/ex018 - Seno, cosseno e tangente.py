import math
ang = int(input('Digite o ângulo que você deseja:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Para o ângulo {}, o seu seno é {:.3f}, o seu cosseno é {:.3f} e sua tangente é {:.3f}.'.format(ang, sen, cos, tan))
#programa que leia um número qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
