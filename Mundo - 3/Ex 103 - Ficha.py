def ficha(nome='Não informado',gols='Não informado'):
    if(nome==''):
        nome='Não informado'
    if gols=='':
        gols='Não informado'
    f= 'O nome do jogador: '+nome+'\nGols marcados: '+ gols


    print(f)

n=input('digite o nome do jogador:\n')
g = input( 'Digite a quantidade de gols marcados:\n' ) 
ficha(n,g )