n=int(input('Digite um número:\n'))
div=[]
for i in range(1 , n+1):
    if n%i==0:
        div.append(i)

if (div.count(n)==1 and div.count(1)==1 and len(div)==2):
    print('O número é primo')
else:
    print('O número não é primo')
    

