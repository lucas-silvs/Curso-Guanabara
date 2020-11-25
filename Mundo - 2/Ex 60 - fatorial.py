n=int(input('Digite um numero:\n'))
f=n
aux=n
while (n!=1):
    f=f*(n-1)
    
    n-=1

print(f'A fatorial de {aux} é: {f}')