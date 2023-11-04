pilha = []
expressao = str(input('Digite a expressão: '))
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(expressao) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está CORRETA!')
else:
    print('Sua expressão está ERRADA!')
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
# expressão passada está com os parênteses abertos e fechados na ordem correta.
