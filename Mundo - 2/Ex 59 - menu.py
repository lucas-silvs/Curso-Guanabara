c=0
n1=int(input('Digite o valor 1:\n'))
n2=int(input('Digite o valor 2:\n'))

while c!=5:

    
    c=int(input('''
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa\n'''))

    if (c==1):
        print(f'A soma de {n1} com {n2} é igual a: {n1+n2}')
    if (c==2):
        print(f'A multiplicação de {n1} com {n2} é igual a: {n1*n2}')
    if (c==3):
        if(n1>n2):
            print(f'O maior é o {n1}')
        else:
            print(f'O maior é o {n2}')
    if(c==4):
        n1=int(input('Digite o novo valor 1:\n'))
        n2=int(input('Digite o novo valor 2:\n'))
        

            