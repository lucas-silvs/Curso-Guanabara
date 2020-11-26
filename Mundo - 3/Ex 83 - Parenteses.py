p=[]

expresão=input('Digite a expressão:\n')
correto=False
for i in expresão:
    if i=='(':
        p.append(i)
    elif i==')':
        p.append(i)
print(p)
while p!=[]:
    
    if(p[0]=='(' and p[len(p)-1]==')'):
        correto=True
        del(p[0])
        del(p[len(p)-1])
    else:
        correto = False
        break

if correto ==True:
    print('Os parenteses estão corretos')
else:
    print('Os parenteses estão incorretos')    

    
