import random as r
n = r.randint(0,5)

usuario = int(input('Digite o número que acredite ser o que o computador escolheu:\n'))

if (n==usuario):
    print('Parabens, vc acertou!!!')
else:
    print('Que pena, vc errou ;-;')