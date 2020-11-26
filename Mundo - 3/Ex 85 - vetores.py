l=[]
p=[]
im=[]
for i in range(7):
    n=int(input('Digite um número:\n'))

    if(n%2==0):
        p.append(n)
    else:
        im.append(n)

l.append(sorted(p))
l.append(sorted(im))

print(f'Numeros pares:\n{l[0]}\nNúmeros impares:\n{l[1]}')