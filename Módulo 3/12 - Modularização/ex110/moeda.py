def aumentar(preco=0, taxa=0, formato=False):
    resultado = preco + (preco * taxa / 100)
    return resultado if formato is False else moeda(resultado)


def diminuir(preco=0, taxa=0, formato=False):
    resultado = preco - (preco * taxa / 100)
    return resultado if formato is False else moeda(resultado)


def dobro(preco=0, formato=False):
    resultado = preco * 2
    return resultado if formato is False else moeda(resultado)


def metade(preco=0, formato=False):
    resultado = preco / 2
    return resultado if formato is False else moeda(resultado)


def moeda(preco=0, real='R$'):
    return f'{real}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, aumento=10, desconto=5):
    resultado = ''
    resultado += f'O valor do produto é {moeda(preco)}.\n'
    resultado += f'O valor com {aumento}% de aumento é {aumentar(preco, aumento, True)}.\n'
    resultado += f'O valor com {desconto}% de desconto é {diminuir(preco, desconto, True)}.\n'
    resultado += f'O dobro do valor é {dobro(preco, True)}.\n'
    resultado += f'A metade do valor é {metade(preco, True)}.'
    return resultado
