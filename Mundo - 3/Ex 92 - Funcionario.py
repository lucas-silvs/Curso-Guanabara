from datetime import date
cadastro=dict()
cadastro ['nome'] = input('Digite o nome do funcionário:\n')
cadastro ['nascimento'] = int(input('Digite o ano de nascimento:\n'))
cadastro ['CTPS'] = int(input('Digite o CTPS:'))
anoatual= date.today()
idade = anoatual.year -cadastro ['nascimento']
if cadastro ['CTPS']!=0:
    cadastro['ano contratação'] = int(input('Digite o ano de contratação:\n'))
    cadastro['salário'] = float(input('digite o salário:\n'))
    dpos = anoatual.year - cadastro['ano contratação']
    dpos = idade+(35 - dpos)

    print(f'''
    Nome funcionário: {cadastro['nome']}
    Idade: {idade}
    CTPS: {cadastro['CTPS']}
    Ano de contratação: {cadastro['ano contratação']}
    Idade de aposentadoria: {dpos}''')
else:
    print(f'''
    Nome funcionário: {cadastro['nome']}
    Idade: {idade}
    CTPS: {cadastro['CTPS']}''')

