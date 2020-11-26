l=[]
for i in range(5):
    l.append(int(input('Digite um número:\n')))

for i in range(len(l)):
    for j in range(len(l)):
        if(l[i]<l[j]):
            aux=l[i]
            l[i]=l[j]
            l[j] = aux
print(l)