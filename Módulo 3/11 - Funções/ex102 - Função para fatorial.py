def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.
    :param num: o número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end=' ')
            if c == 1:
                print('=', end=' ')
            else:
                print('x', end=' ')
    return f


print(fatorial(6, show=True))
print(fatorial(9, show=True))
print(fatorial(4, show=True))
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.
