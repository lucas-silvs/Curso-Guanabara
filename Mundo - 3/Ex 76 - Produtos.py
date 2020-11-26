tupla=('Leite',5,'Arroz',12.50,'Feijão',9.30)
t= '.'*30
for i in range(0,len(tupla)-1,2):
    print(f'{tupla[i]} {t} R$:{tupla[i+1]}')