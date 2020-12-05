 
def leiaint(n):
    aux = 0
    num=''
    while aux == 0:
        try:
            num=int(input(n))
        except (TypeError,ValueError):
            print ('O texto digitado não é um número')
        else:

            return num


def leiafloat(n):
    aux = 0
    num=''
    while aux == 0:
        try:
            num=float(input(n))
        except :
            print ('O texto digitado não é um número')
        else:

            return num



j=leiaint('Digite um  número inteiro:\n')
k = leiafloat('Digite um número real:\n')

print(f'''
Número real digitado: {k}
Numero inteiro digitado: {j}''')




