from random import randint
def somapar(numeros):
    somapar=0
    print('Os números pares da lista são')
    for i in numeros:
        if i % 2 == 0:
            print(i,end=" ")
            somapar+=i

    print(f'\nA soma dos pares da lista é {somapar}') 
    
        


def sorteio():
    numeros = list()
    while len(numeros)!=5:
        sort=randint(0,10)
        if sort not in numeros:
            numeros.append(sort)
    print(numeros)
    somapar(numeros)



sorteio()


