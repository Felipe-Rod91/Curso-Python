# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# – Quantidade de notas
# – Maior nota
# - Menor nota
# – Média da turma
# – Situação (opcional)


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não aceitar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    lista = dict()
    lista['total'] = len(n)
    lista['maior'] = max(n)
    lista['menor'] = min(n)
    lista['média'] = round(sum(n) / len(n), 1)
    if sit:
        if lista['média'] < 6:
            lista['situação'] = 'RUIM'
        elif 6 <= lista['média'] < 8:
            lista['situação'] = 'REGULAR'
        else:
            lista['situação'] = 'BOA'
    return lista


resp = notas(9, 8, 9, sit=True)
print(resp)
