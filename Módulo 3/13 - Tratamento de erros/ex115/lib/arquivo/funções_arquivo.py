from ..interface.funções_interface import título


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'Houve um erro na criação do arquivo {nome}.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Arquivo não pôde ser lido.')
    else:
        título('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<32}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastro(arquivo, nome='Desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('ERRO! Não foi possível cadastrar a pessoa.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()