jogador = dict()
time=[]
n='s'
while n=='s':
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

    ch=''
    while(ch!='s' or ch!='n'):
        ch = input('Deseja cadastrar mais? [S/N]\n').lower()
        if(ch=='s'):
            break
        elif(ch=='n'):
            n='n'
            break






for i in time:
    print(f'''
        Nome do jogador: {i['nome']}
        Gols por partida: {i['qtdegolspartida']}
        Total de gols no campeonato: {i['total']}''')

escolha=''
while escolha!='sair':
    escolha = input('digite o nome do jogador que deseja consultar:\n')
    if i['nome']==escolha in time:
        print(f'{i["nome"]} jogou um total de {i["qtdepartidas"]} partidas:\n')
    for ind,gols in enumerate(i['qtdegolspartida']):
        print(f' Na partida {ind+1} fez {part} gol(s)')