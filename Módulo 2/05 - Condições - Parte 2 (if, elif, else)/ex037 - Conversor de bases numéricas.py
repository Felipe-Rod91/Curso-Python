# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão:')
print('[1] Converter para BINÁRIO.')
print('[2] Converter para OCTAL.')
print('[3] Converter para HEXADECIMAL.')

conv = int(input('Sua opção: '))

if conv == 1:
    print(f'O número {num} em BINÁRIO é {bin(num)[2:]}.')
elif conv == 2:
    print(f'O número {num} em OCTAL é {oct(num)[2:]}.')
elif conv == 3:
    print(f'O número {num} em HEXADECIMAL é {hex(num)[2:]}.')
else:
    print('ERRO! OPÇÃO INVÁLIDA!')
