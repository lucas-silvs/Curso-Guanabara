from  interface import  *
def arquivoexiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome,'wt+')
    except:
        print('Houve algum ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerarquivo(nome):
    try:
        a= open(nome,'rt')
    except:
        print('Erro ao ler o arquivo')

    else:
        cabecalho('Pessoas cadastradas')
        for i in a:
            dado = i.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'Nome: {dado[0]:<30} Idade: {dado[1]}')
    finally:
        a.close()

def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a=open(arq,'at')
    except:
        print('Erro ao cadastrar')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve algum erro na escrita')
        else:
            print('Novo Registro {nome}')
        finally:
            a.close()




