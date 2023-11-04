def voto(ano):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


nasc = int(input('Digite o ano de nascimmento: '))
print(voto(1931))
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
