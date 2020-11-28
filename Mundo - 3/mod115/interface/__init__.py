def leiaint(n):
    aux = 0
    num = ''
    while aux == 0:
        try:
            num = int(input(n))
        except (TypeError, ValueError):
            print('O texto digitado não é um número')
        else:

            return num


def linha(t=42):
    return '-' * t


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")

    for c in lista:
        print(c)
    print(linha())
    opc=0
    opc = leiaint('Digite sua opção\n')
    return  opc