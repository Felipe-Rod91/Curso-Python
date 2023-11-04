num = int(input('Diga um número: '))
print('A tabuada de {} é:'.format(num))
for tab in range(1, 11, 1):
    print('{} x {} = {}'.format(num, tab, num * tab))
#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
