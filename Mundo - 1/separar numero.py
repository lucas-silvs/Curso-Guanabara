num = int(input("Digite um número de 0 a 9999\n"))
m= num //1000
num=num-(m*1000)
c = num//100
num = num - (c*100)
d = num // 10
num = num - (d*10)
u=num

print(f'Milhar: {m}\nCentena: {c}\nDezena: {d}\nUnidade: {u}')