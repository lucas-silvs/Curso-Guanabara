
aluno=dict()
aluno['Nome'] = input('Digite seu nome:\n')
aluno['Nota'] = float(input('Digite a média da nota:\n'))

print(f'Aluno: {aluno["Nome"]} : Média: {aluno["Nota"]}')

if(aluno['Nota']<5):
    print('O aluno está reprovado')
elif(aluno['Nota']>=5 and aluno['Nota']<7):
    print('Aluno em recuperação')
else:
    print('Aluno aprovado')
