def fatorial(num=0, show=0):

    '''
    Digite o valor do número a ser fatorado primeiro
    e depois digite 1 caso queira ver o processo de calculo,
    ou digite 0 caso não queira ver o processo de calculo
    '''
    fato=num

    for i in range(num-1,0,-1):
        if(show == 1):
            print(f'{fato} X {i} = {fato*i}')
        fato = fato*i
    
    return fato

a = int(input('Digite o numero para fatorar:\n'))
b = int(input('Caso deseje ver os calculos, digite 1, senão digite 0:\n'))

fat = fatorial(a,b)

print(f'O resultado final da fatorial de {a} é: {fat}')

     
