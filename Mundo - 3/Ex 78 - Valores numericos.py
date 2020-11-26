n=[]
for i in range(5):
    n.append(int(input('Digite um número:\n')))

print(f'''
O maior valor da lista é: {max(n)} que está na posição {n.index(max(n))}
O menor valor da lista: {min(n)} que está na posição {n.index(min(n))}''')