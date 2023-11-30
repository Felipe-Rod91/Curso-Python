#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Diga um número: '))
print(f'A tabuada de {num} é:')
for tab in range(1, 11, 1):
    print(f'{num} x {tab} = {num * tab}')
