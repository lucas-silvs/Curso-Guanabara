import random as r
alunos= input('Digite o nome dos alunos\n').split()


ordem= r.choice(alunos)

print(f'O primeiro grupo será: {ordem}')
alunos.remove(ordem)

ordem= r.choice(alunos)

print(f'O segundo grupo será: {ordem}')
alunos.remove(ordem)

ordem= r.choice(alunos)

print(f'O terceiro grupo será: {ordem}')
alunos.remove(ordem)
ordem= r.choice(alunos)
print(f'O quarto grupo será: {ordem}')

r.shuffle