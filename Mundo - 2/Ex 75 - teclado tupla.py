n1 = int(input('Digite un número:\n'))
n2 = int(input('Digite un número:\n'))
n3 = int(input('Digite un número:\n'))
n4 = int(input('Digite un número:\n'))

t=(n1,n2,n3,n4)

print(f'''
Quantidade de números 9 digitados: {t.count(9)}''')
if(t.count(3)>0):
    print(f'a posição do primeiro número 3: {t.index(3)+1}''')
else:
    print('Nenhum número 3 foi digitado')
        

print('Os números pares digitados:')
for i in t:
    if(i%2==0):
        print(i)