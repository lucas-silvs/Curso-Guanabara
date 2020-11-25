qtdeh=0
mais=0
qtdem=0

c='S'

while c=='S':
    idade = input('Digite a idade:\n')
    while(idade.isdigit()==False):
        idade = input('Digite a idade:\n')
    idade=int(idade)
    s=''
    while((s!='m') or (s!='f')):
        s=input('''Digite o sexo da pessoa: [M/F]\n''').lower()
        if(s=='m' or s=='f'):
            break

    if(idade>18):
        mais+=1
    if(s=='m'):
        qtdeh+=1
    if(s=='f' and idade<20):
        qtdem+=1

    ch=''
    while(ch!='S' or ch!='N'):
        ch=input('''Deseja continuar? [S/N]\n''').upper()
        if(ch=='N'):
            c='N'
            break
        elif(ch=='S'):
            break
    

    

print(f'''
Quantidade de pessoas com mais de 18 anos: {mais}
Quantidade de homens cadastrados: {qtdeh}
Quantidade de mulheres com menos de 20 anos: {qtdem}''')
