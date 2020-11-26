l=[]
i=[]
p=[]

n='s'
while n == 's':
    num=int(input('Digite um número:\n'))
    l.append(num)
    if num%2==0:
        p.append(num)
    else:
        i.append(num)
    
    ch=''
    while ch!='s' or ch!='n':
        ch=input('Deseja Continuar? [S/N\n').lower()
        if(ch=='n'):
            n='n'
            break
        elif(ch=='s'):
            break

print('Lista digitada:\n')
for j in l:
    print(j,end=' ')

print('\nValores pares da lista:\n')
for pares in p:
    print(pares, end=' ')
print('\nValores impares na lista:\n')
for impares in i:
    print(impares,end = ' ')