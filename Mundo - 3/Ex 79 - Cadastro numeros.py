l=[]

n='s'

while n =='s':
    num=int(input('Digite um valor:\n'))
    if(num not in l):
        l.append(num)
    
    c=''
    while(c!='n' or c!='s' ):
        c=input('Deseja continuar? [S/N]\n').lower()

        if (c=='n'):
            n=c
            break
        elif(c=='s'):
            break
        
print('Os valores digitados em ordem crescente:\n')
for i in sorted(l):
    print(i, end=' ')