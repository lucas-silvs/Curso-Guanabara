import random as r
alunos= input('Digite o nome dos alunos\n').split()


alunoescolhido= r.choice(alunos)

print(f'O aluno escolhido foi o {alunoescolhido}')