brasileiro = ('Atletico-MG', 'Flamengo', 'São Paulo', 'Internacional',
'Fluminense','Palmeiras','Santos','Grêmio','Corinthians','Athletico-PR',
'Bahia','Fortaleza','Bragantino','Ceará SC','Sport Recife','Vasco da Gama',
'Coritiba','Botafogo','Goiás')

print('Os 5 primeiros colocados:')
for i in range(5):
    print(brasileiro[i])

print('Os 4 ultimos colocados')
for i in range(len(brasileiro)-4,len(brasileiro)):
    print(brasileiro[i])

print('Times em ordem alfabética:\n')
for time in sorted(brasileiro):
    print(time)

print('\nChapecoense:\n')
ind=23
for n,time in enumerate(brasileiro):
    if(time=='Chapecoense'):
        ind=n

if(ind!=23):
    print(f'Chapecoense está classificado no Brasileirão na posição {ind+1}')
else:
    print('Chapecoense não está no Brasileirão')

        
    