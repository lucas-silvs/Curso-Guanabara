preco = float(input('Digite o valor do produto:\n'))

chose=int(input('''Digite a forma de pagamento\n
1-A vista no dinheiro/cheque\n
2-A vista no cartão\n
3-em até 2x no cartão\n
4-3x ou mais no cartão:\n'''))

if chose==1:
    print(f'O valor final do pagamento a vista/cheque: {preco-(preco*0.1)}')

elif chose==2:
    print(f'O valor final do pagamento a vista no cartão: {preco-(preco*0.05)}')

elif chose==3:
    print(f'O valor final do pagamento em até 2x no cartão: {preco}')

elif chose==4:
    print(f'O valor final do pagamento em 3x ou mais no cartão: {preco+(preco*0.2)}')
    
    