l=[]
e='s'

while e=='s':
    
    l.append(int(input('Digite um número:\n')))

    ch=''
    while ch!='s' or ch!='n': 
        ch=input('Deseja continuar? [S/N]\n').lower()
        if(ch=='s'):
            break
        elif(ch == 'n'):
            e='n'
            break

print(f'Quantidade de números digitados: {len(l)}')
print('A lista ordenada em forma decrescente')
l.sort(reverse=True)
for i in l:
    print(i,end=' ')
if 5 in l:
    print(f'\nO valor 5 foi digitado na lista e está na posição: {l.index(5)}')
else:
    print('\nO valor 5 não foi digitado na lista')

