def leiaint(msg):
    valor = 0
    ok = False
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um valor inteiro.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só
# que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
