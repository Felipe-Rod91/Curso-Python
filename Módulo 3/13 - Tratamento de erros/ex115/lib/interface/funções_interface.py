def leia_int(txt):
    while True:
        try:
            valor = int(input(txt))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;33mUsuário preferiu não digitar o número.\033[m')
            return 0
        else:
            return valor


def linha(tam=40):
    return '-' * tam


def título(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    título('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opção = leia_int('\033[32mSua opção: \033[m')
    return opção
