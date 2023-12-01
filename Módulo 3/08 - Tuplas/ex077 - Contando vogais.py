# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado',
            'Trabalhador', 'Futuro')
for word in palavras:
    print(f'\nA palavra {word.upper()} tem as vogais', end=' ')
    for letra in word:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
