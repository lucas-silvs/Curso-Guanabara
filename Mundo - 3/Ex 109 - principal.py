from utilidadesCeV import moedas
choice = False
mod = float(input('Digite o preço: R$ '))
c = input('Deseja Formatar [S/N]\n').lower()

if c == 's':
    choice=True


print(f'''
A metade de {moedas.moeda(mod)}: {moedas.metade(mod,choice)}
O dobro de {moedas.moeda(mod)}: {moedas.dobro(mod,choice)}
Aumentando 10%, temos {moedas.aumentar(mod,10,choice)}
Reduzindo 13%, temos {moedas.diminuir(mod,13,choice)}''')