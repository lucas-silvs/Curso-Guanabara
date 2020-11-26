b=[]

c='s'

while c=='s':
    al=[]
    notas=[]
    al.append(input('Digite o nome do aluno:\n'))
    notas.append(float(input('Digite o valor da nota 1:\n')))
    notas.append(float(input('Digite o valor da nota 2:\n')))
    al.append(notas)
    al.append((notas[0]+notas[1])/2)
    b.append(al)

    ch=''
    while ch!='s' or ch!='n':
        ch = input('Deseja continuar? [S/N]\n').lower()
        if(ch=='s'):
            break
        elif(ch=='n'):
            c='n'
            break

aux=0

while aux==0:
    a = input('Digite o nome do aluno ou digite "sair" para sair:\n')
    if a == 'sair':
        break
    if a not in b:
        print('Digite um nome valido')
    for i in b:
        if(a in i[0]):
            print(f'Nome aluno: {i[0]}\nNota 1: {i[1][0]}\nNota 2: {i[1][1]}\nMédia: {(i[2])/2:.2f}')

    