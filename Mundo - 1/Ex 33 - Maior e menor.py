n1 = int(input('Digite um número:\n'))
n2 = int(input('Digite um número:\n'))
n3 = int(input('Digite um número:\n'))

if(n1 > n2 and n2> n3):
    print(f'menor:{n3}\n maior: {n1}')

elif(n1 > n2 and n2< n3):
    print(f'menor:{n2}\n maior: {n1}')

elif(n1 < n2 and n2< n3):
    print(f'menor:{n1}\n maior: {n3}')

elif(n1 > n2 and n2< n3):
    print(f'menor:{n2}\n maior: {n3}')

elif(n1 < n2 and n1> n3):
    print(f'menor:{n3}\n maior: {n2}')

elif(n3 < n2 and n1< n3):
    print(f'menor:{n1}\n maior: {n2}')