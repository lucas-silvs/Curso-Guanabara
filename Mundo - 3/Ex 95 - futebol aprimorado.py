jogador = dict()
time=[]
n=0
while n==0:
    ch=''
    jogador = dict()
    jogador['nome']= input('Digite o nome do jogador:\n')
    jogador['qtdepartidas'] = int(input('Digite a quantidade de partidas que o jogador participou:\n'))
    partidas=[]
    f=0
    for i in range(jogador['qtdepartidas']):
        n= int(input(f'Quantidade de gols feitos na partida {i+1}:\n'))
        f=f+n
        partidas.append(n)

    jogador['qtdegolspartida'] = partidas
    jogador['total'] = f
    time.append(jogador)

    while ch!='s' and ch!='n':
        ch = input('Deseja cadastrar mais? [S/N]\n').lower()
        if(ch=='n'):
            n=1
            break
        elif(ch=='s'):
            n=0
            break
               







for j in time:
    print(f'''
        Nome do jogador: {j['nome']}
        Gols por partida: {j['qtdegolspartida']}
        Total de gols no campeonato: {j['total']}''')

escolha=''
while escolha!='sair':
    escolha = input('digite o nome do jogador que deseja consultar:\n')
    if escolha=='sair':
        break
    for k in time:
        if k['nome']==escolha:
            print(f'{k["nome"]} jogou um total de {k["qtdepartidas"]} partidas:\n')
    for ind,gols in enumerate(k['qtdegolspartida']):
        print(f' Na partida {ind+1} fez {gols} gol(s)')
    

