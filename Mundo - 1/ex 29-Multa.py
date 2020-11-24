vel=float(input('Digite a velocidade:\n'))

if(vel>80.00):
    multa = (vel - 80.00) * 7
    print(f'O valor da multa a pagar será de: R${multa:.2f}')