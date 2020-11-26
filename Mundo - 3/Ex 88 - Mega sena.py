from random import randint
l=[]
n=int(input('Digite a quantidade de jogos:\n'))

for i in range(n):
    aux=[]
    while len(aux)<6:
        nu = randint(1,60)
        if nu not in aux:
            aux.append(nu)

    l.append(aux)

for i in range(n):
    print(f'Sequencia do {i+1}º Jogo: {l[i]}')