# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista_numerica = []
for c in range(0, 5):
    num = int(input(f'Digite o número: '))
    if c == 0 or num > lista_numerica[-1]:
        lista_numerica.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista_numerica):
            if c <= lista_numerica[pos]:
                lista_numerica.insert(pos, num)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print(f'Os valores em ordem foram {lista_numerica}.')
