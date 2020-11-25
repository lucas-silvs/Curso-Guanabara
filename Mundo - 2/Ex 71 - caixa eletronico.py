valorsaque=int(input('Digite o valor de saque:\n'))

cinq=0
vin=0
dez=0
um=0

while valorsaque!=0:
    if valorsaque>=50:
        valorsaque=valorsaque-50
        cinq+=1
    elif valorsaque >=20 and valorsaque<50:
        valorsaque = valorsaque - 20
        vin+=1
    elif valorsaque>=10 and valorsaque<20:
        valorsaque = valorsaque-10
        dez+=1
    elif valorsaque<10:
        valorsaque=valorsaque-1
        um+=1

print(f'''
Quantidade de celulas entregues:
R$50,00: {cinq}
R$20,00: {vin}
R$10,00: {dez}
R$1,00: {um}''')
