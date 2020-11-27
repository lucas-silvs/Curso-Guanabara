pessoas=[]

n='s'
media=0
while n=='s':
    cad=dict()
    cad['nome'] = input('Digite seu nome:\n')
    cad['sexo'] = input('Seu sexo: [F/M]\n').upper()
    cad['idade'] = int(input('Sua idade:\n'))
    media = media + cad['idade']
    pessoas.append(cad)
    
    ch=''
    while(ch!='s' or ch!='n'):
        ch = input('Deseja cadastrar mais? [S/N]\n').lower()
        if(ch=='s'):
            break
        elif(ch=='n'):
            n='n'
            break


print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
#B - a media das idades do grupo
media = media / len(pessoas)

print(f'A media de idades das pessoas cadastradas é: {media}')

#C e D - cadastros do sexo feminino e com a idade acima da media
mulheres=[]
idadeacima=[]

print(f'{"="*20} Pessoas cadastradas {"="*20}')
for p in pessoas:
    if p['sexo'] == 'F':
        mulheres.append(p)
    if p['idade'] > media:
        idadeacima.append(p)
    print(f'''
    Nome: {p['nome']}
    Sexo: {p['sexo']}
    idade: {p['idade']}''')

print(f'{"="*20} Pessoas com idade acima da média {"="*20}')
for p in idadeacima:
     print(f'''
    Nome: {p['nome']}
    Sexo: {p['sexo']}
    idade: {p['idade']}''')

print(f'{"="*20} Pessoas cadastradas do sexo feminino {"="*20}')
for p in mulheres:
     print(f'''
    Nome: {p['nome']}
    Sexo: {p['sexo']}
    idade: {p['idade']}''')




