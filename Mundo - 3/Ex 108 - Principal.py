from utilidadesCeV import moedas

mod = float(input('Digite o preço: R$ '))

print(f'''
A metade de {moedas.moeda(mod)}: {moedas.moeda(moedas.metade(mod))}
O dobro de {moedas.moeda(mod)}: {moedas.moeda(moedas.dobro(mod))}
Aumentando 10%, temos {moedas.moeda(moedas.aumentar(mod,10))}
Reduzindo 13%, temos {moedas.moeda(moedas.diminuir(mod,13))}''')