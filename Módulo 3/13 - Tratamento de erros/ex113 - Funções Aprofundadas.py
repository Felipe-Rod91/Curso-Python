# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
# tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leia_int(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;33mUsuário preferiu não digitar o número.\033[m')
            return 0
        else:
            return valor


def leia_float(msg):
    while True:
        try:
            valor = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;33mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return valor


numero_inteiro = leia_int('Digite um número inteiro: ')
numero_real = leia_float('Digite um número real: ')
print(f'O valor inteiro foi {numero_inteiro} e o real foi {numero_real}.')
