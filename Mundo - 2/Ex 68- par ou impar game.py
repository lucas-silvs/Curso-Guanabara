from random import randint
v=0
qtdev=0

while v==0:
    if(v==1):
        break
    c=int(input('''
    Escolha 1-par ou 2-impar\n'''))
    pc=randint(0,5)
    pl=int(input('Escolha um número de 0 a 5\n'))

    if(((pc+pl)%2==0 and c==1) or ((pc+pl)%2!=0 and c==2)):
        print('''PARABENS VOÇÊ VENCEU!!!''')
        qtdev+=1
    else:
        print('''QUE PENA, VOÇÊ PERDEU''')
        v=1

print(f'''Quantidade de vitórias consecutivas: {qtdev}''')
