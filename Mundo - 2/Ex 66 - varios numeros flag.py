n=0
soma=0
qtde=0

while(n!=999):
    n=int(input('Digite um número:\n'))
    qtde+=1
    soma=soma+n

print(f'''
Quantidade de número digitados: {qtde}
soma desses números: {soma-999}''')