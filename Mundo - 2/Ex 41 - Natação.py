import datetime
anonasci=int(input('Digite a data de nascimento do atleta:\n'))

idade = datetime.date.today().year - anonasci

if(idade<10):
    print('Categoria Mirim')
elif (idade>9 and idade<15):
    print('Categoria Infantil')
elif idade>14 and idade<20:
    print('Categoria junior')
elif idade==20:
    print('categoria sênior')
elif idade>20:
    print('Categoria master')