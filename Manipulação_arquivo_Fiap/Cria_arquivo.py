import  json
import  os

dici = { 'alooo':[ '45','1,54','80'],
'ulaaa': ['33','1,60','80']
}
aux= dict()
if os.path.exists('jason.json'):
    with open('jason.json','a') as banco:
        json.dump(dici,banco)
else:
    with open('jason.json','w') as banco:
        json.dump(dici,banco)


with open('jason.json','r') as banco:
    aux= json.load(banco)

for nome,dados in aux.items():
    print(f'Nome: {nome}\nIdade: {dados[0]}\nAltura: {dados[1]}\nPeso: {dados[2]}')
