n=int(input('Digite a qtde de números:\n'))

i=1
pr=0
sc=1
print(0)
print(1)
    
while(i<=n-2):
    aux=sc 
    sc = sc+pr
    pr=aux
    print(sc)
    i+=1

    
    
