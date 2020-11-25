maior=0
menor = 0

for i in range(5):
    peso = float(input('Digite o peso:\n'))
    if(i==0):
        maior = peso
        menor = peso
    else:
        if(peso>maior):
            maior =peso
        elif(peso<menor):
            menor= peso

print(f'''Maior peso digitado: {maior}
Menor peso digitado: {menor}''')
