nome = input("Digite seu nome completo:\n")
up= nome.upper()
low= nome.lower()
ltotal = len(nome.replace(" ",""))
lnome = nome.split()
lnome= len(lnome[0])
print(f'Nome com letras maiusculas: {up}\nNome com letras minusculas: {low}\nQtde de letras ao todo: {str(ltotal)}\nQtde de letras no primeiro nome: {str(lnome)}')