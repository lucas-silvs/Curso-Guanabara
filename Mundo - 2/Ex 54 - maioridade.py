from datetime import date
qtdemaiores=0
qtdemenores=0

for i in range(7):
    datanascimento=int(input('Digite o ano de nascimento:\n'))
    idade = date.today().year - datanascimento
    if(idade>=21):
        qtdemaiores+=1
    else:
        qtdemenores+=1

print(f'''Quantidade de pessoa menores de idade: {qtdemenores}
Quantidade de pessoa maiores de idade:{qtdemaiores}''')
    