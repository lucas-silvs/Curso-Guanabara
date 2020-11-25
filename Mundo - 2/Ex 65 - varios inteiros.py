maior=0
menor=0
media=0
qtde=0
c='S'

while(c=='S'):
    n=int(input('Digite um número\n'))
    if(qtde==0):
        menor=n
        maior=n
    qtde+=1
    media=media+n

    if(n>maior):
        maior = n
    elif(n<menor):
        menor=n

    c=input('''
    Deseja continuar [S/N]\n''')

print(f'''
Média entre os valores: {(media/qtde):.2f}
o maior valor: {maior}
o menor valor: {menor}''')