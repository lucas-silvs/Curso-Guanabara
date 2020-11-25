n=0
while n>=0:
    n=int(input('Digite um número para a tabuada\n'))
    if(n<0):
        break
    i=1
    while i<=10:
        print(f'{n} X {i} = {n*i}')
        i+=1