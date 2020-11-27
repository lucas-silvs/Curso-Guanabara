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

print(f'''
Nome do jogador: {jogador['nome']}
Gols por partida: {jogador['qtdegolspartida']}
Total de gols no campeonato: {jogador['total']}''')

print(f'{jogador["nome"]} jogou um total de {jogador["qtdepartidas"]} partidas:\n')
for i,part in enumerate(partidas):
    print(f' Na partida {i+1} fez {part} gol(s)')