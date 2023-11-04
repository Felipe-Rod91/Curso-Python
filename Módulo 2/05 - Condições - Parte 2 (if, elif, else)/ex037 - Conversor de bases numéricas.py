num = int(input('Digite um número inteiro: '))
print('Escola uma das bases para conversão:')
print('[1] Converter para BINÁRIO.')
print('[2] Converter para OCTAL.')
print('[3] Converter para HEXADECIMAL.')
conv = int(input('Sua opção: '))
if conv == 1:
    print('O número {} em BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif conv == 2:
    print('O número {} em OCTAL é {}.'.format(num, oct(num)[2:]))
elif conv == 3:
    print('O número {} em HEXADECIMAL é {}.'.format(num, hex(num)[2:]))
else:
    print('ERRO! OPÇÃO INVÁLIDA!')
#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
#de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
