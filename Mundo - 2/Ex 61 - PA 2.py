
razao = float(input('Digite o valor da razão:\n'))
p =  float(input('Digite o primeiro termo:\n'))
aux=1
r=0
t=10
t2=1
while(t2!=0):
    while(aux<t):
    
        pl=p + razao*aux
        print(pl)
        aux+=1
    
    t2=int(input('Quer mostrar mais \n'))
    t=t+t2