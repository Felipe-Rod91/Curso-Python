# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livro', 34.9)
print('-=' * 20)
print(f'{"LISTA DE MATERIAL ESCOLAR":^40}')
print('-=' * 20)
for n in range(len(lista)):
    if n % 2 == 0:
        print(f'{lista[n]:.<30}', end='')
    if n % 2 == 1:
        print(f'R${lista[n]:>6.2f}')
print('-' * 40)
