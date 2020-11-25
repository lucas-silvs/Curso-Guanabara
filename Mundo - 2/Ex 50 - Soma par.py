s=0
for i in range(6):
    n=int(input('Digite um número:\n'))
    if(n%2==0):
        s=s+n

print(f'Soma dos número impares digitados: {s}')