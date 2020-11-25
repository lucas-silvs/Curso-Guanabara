import random as r
res=0
pal=1
n = r.randint(0,10)
while res==0:

    

    usuario = int(input('Digite o número que acredite ser o que o computador escolheu:\n'))

    if (n==usuario):
        print('Parabens, vc acertou!!!')
        print(f'qtde de palpites necessarios: {pal}')
        res=1
    else:
        print('Que pena, vc errou ;-;')
        pal+=1