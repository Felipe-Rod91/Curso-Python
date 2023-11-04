import moeda
valor = float(input('Digite um valor: '))
porcent = int(input('Digite uma porcentagem: '))
print(f'O valor de {valor} aumentado em 10% é {moeda.aumentar(valor, porcent)}.')
print(f'O valor de {valor} diminuído em 10% é {moeda.diminuir(valor, porcent)}.')
print(f'O dobro de {valor} é {moeda.dobro(valor)}.')
print(f'A metade de {valor} é {moeda.metade(valor)}.')
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça
# também um programa que importe esse módulo e use algumas dessas funções.
