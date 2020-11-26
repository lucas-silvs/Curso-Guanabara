matriz=[]
linha=[]
somapar = 0
for i in range(9):
    n=int(input('Digite os numeros que serão adicionado a matriz:\n'))
    linha.append(n)
    if(i+1==3 or i+1==6 or i+1==9):
        matriz.append(linha)
        linha=[]
    

print(f'''
[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]''')

for i in matriz:
    for j in i:
        if j%2==0:
            somapar = somapar+j

print(f'''
A soma dos pares da matriz: {somapar}
A soma dos valores da terceira coluna: {matriz[0][2]+matriz[1][2]+matriz[2][2]  }
O maior valor da segunda linha: {max(matriz[1])}''')




