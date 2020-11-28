from mod115.interface import *
from  mod115.arquivos import *

arquivo = 'armazenamento.txt'
cabecalho('Testando')


if not arquivoexiste(arquivo):
    criararquivo(arquivo)
while True:
    escolha = menu(['1 - Para add pesso','2 - listar cadastros','3 - Sair'])
    if escolha == 1:
        cabecalho('Cadastro de cliente:')
        nome=input('Digite o nome\n')
        idade = leiaint('Digite a idade:\n')
        cadastrar(arquivo,nome,idade)

    elif escolha == 2:
        lerarquivo(arquivo)


    elif escolha == 3:
        break
    else:
        print('Opção invalida\n')