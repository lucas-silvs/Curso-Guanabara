km = int(input('Digite a distancia da viagem:\n'))
valor = 0
if(km>200):
    valor = km * 0.45
else:
    valor = km * 0.50
print(f'O valor da viagem será de R${valor:.2f}')