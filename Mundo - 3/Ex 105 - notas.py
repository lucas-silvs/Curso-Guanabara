def notas(*n, c=False):

    '''
    Essa função recebe uma lista de notas de alunos, cria um dict e 
    add as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A media da turma
    - A situação

    '''
    aluno=dict()
    maior =0
    menor = 0
    aluno['Quantidades de notas'] = len(n)
    m=0
    for i in range(len(n)):
        if i==0:
            maior=n[i]
            menor=n[i]
        elif(n[i]<menor):
            menor=n[i]
        elif(n[i]>maior):
            maior=n[i]
        m=m+n[i]
    aluno['Maior'] = maior
    aluno['Menor'] = menor
    aluno['Media'] = m/len(n)

    if c==True:
        aluno['Situação'] = ''

        if  m/len(n) <5:
            aluno['Situacao'] = 'Reprovado'
        elif m/len(n)>5 and m/len(n)<6:
            aluno['Situacao'] = 'Recuperação'
        elif m/len(n)>=6:
            aluno['Situacao'] = 'Aprovado'

    return aluno

f = notas(5,2,9,c=True)
print(f)

