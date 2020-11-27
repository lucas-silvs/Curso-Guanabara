from random import randint
p=dict()
p={'jogador 1': randint(1,6),
'jogador 2': randint(1,6),
'jogador 3': randint(1,6),
'jogador 4': randint(1,6)}


for f in p:
    print(f'O {f} tirou {p[f]}')
l=1
for d in sorted(p, key= p.get, reverse= True):
    print(f'{l}º Lugar: {d} com {p[d]} ')
    l+=1
    
     