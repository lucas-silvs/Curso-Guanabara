import random as r
c = r.randint(1,3)

esc=int(input('''Escolha uma mão:\n'
1 - Pedra\n
2 - Papel\n
3 - Tesoura\n'''))

if(esc==1 and c==3):
    print('Voce ganhou ')
elif esc==1 and c ==1:
    print('Empate')

elif esc==2 and c==1:
    print('Voce ganhou')
elif esc==2 and c ==2:
    print('Empate')

elif esc==3 and c==2:
    print('Voce ganhou')
elif esc==3 and c ==3:
    print('Empate')

else:
    print('Voce perdeu')


