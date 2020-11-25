s=''
while s!='M' or s!='F':
    s=input('Digite o sexo:\n')
    if (s=='M' or s=='F'):
        break
    else:
        print('Digite novamente',s)
    


print(f'Sexo digitado: {s}')