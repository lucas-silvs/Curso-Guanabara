total=0
qtdemais=0
nomebarato=''
precobarato=0

c='S'
ocasiao=1
while c=='S':
    
    nome=input('Digite o nome do produto:\n')

    preco=input('Digite o valor do produto:\n')
    while preco.isdigit()==False:
        preco=input('Digite o valor do produto:\n')
    preco=float(preco)

    if preco>1000:
        qtdemais+=1
    
    if ocasiao==1:
        nomebarato=nome
        precobarato=preco
        ocasiao+=1
    
    if preco<precobarato:
        nomebarato=nome
        precobarato=preco


    total=total+preco
    ch=''
    
    while ch!='s' or ch!='n':
        ch=input('Deseja continuar? [S/N]\n').lower()
        if(ch=='s'):
            break
        elif(ch=='n'):
            c='N'
            break


print(f'''
Total gasto: {total}
Quantidade de produtos acima de R$1000,00: {qtdemais}
O nome do produto mais barato: {nomebarato}''')