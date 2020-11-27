from utilidadesCeV import moedas

mod = float(input('Digite o preço: R$ '))

print(f'''
A metade de {mod}: {moedas.metade(mod)}
O dobro de {mod}: {moedas.dobro(mod)}
Aumentando 10%, temos {moedas.aumentar(mod,10)}
Reduzindo 13%, temos {moedas.diminuir(mod,13)}''')