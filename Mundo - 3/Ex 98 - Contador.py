from time import sleep
def contador():
    print('Contagem de 1 até 10:\n')

    for i in range(1,11,1):
        print(i)
        sleep(1)
    print('Contagem de 10 até 0, com passo de 2:\n')
    for i in range(10,0,-2):
        print(i)
        sleep(1)
    
    ini= int(input('Digite o inicio da contagem:\n'))
    fim= int(input('Digite o fim da contagem:\n'))
    passo = int(input('Digite o passo da contagem:\n'))
    print(f'Contagem de {ini} até {fim}, com passo de {passo}:\n')

    if passo == 0:
        passo=1
    elif (passo <0):
        passo*=-1

    if ini< fim:
            for i in range(ini,fim+1,passo):
                print(i)
                sleep(1)
    else:
        for i in range(ini,fim,-passo):
            print(i)
            sleep(1)
    



contador()
