n1 = float(input('Digite a nota 1:\n'))
n2 = float(input('Digite a nota 2:\n'))

media = (n1+n2)/2

if (media<5.0):
    print('Reprovado')
elif media>5 and media <7.0:
    print('Recuperação')
else:
    print('Aprovado')