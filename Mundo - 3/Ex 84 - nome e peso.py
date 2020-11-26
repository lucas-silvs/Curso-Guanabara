l=[]

n='s'

while n =='s':
    p=[]
    p.append(input('Digite o nome:\n'))
    p.append(int(input('Digite o peso da pessoa:\n')))
    l.append(p)

    ch=''
    while ch!='s' or ch!='n':
        ch = input('Deseja continuar? [S/N]\n').lower()
        if ch=='s':
            break
        elif ch=='n':
            n='n'
            break
menor=0
maior=0

print(l)
for i in l:
    if l.index(i)==0:
        menor=i[1]
        maior=i[1]
    
    if i[1] < menor:
        menor = i[1]
    elif i[1] > maior:
        maior = i[1]
lmenor=[]
lmaior=[]
for i in l:
    if(i[1]==menor):
        lmenor.append(i)
    elif(i[1])==maior:
        lmaior.append(i)


    

print(f' pessoas com menor peso:')
for j in lmenor:
    print(f'Nome: {j[0]} Peso: {j[1]}')
print(f' pessoa com maior peso:')
for k in lmaior:
    print(f'Nome: {k[0]} Peso: {k[1]}')
print(f'Quantidade total de pessoas: {len(l)}')




