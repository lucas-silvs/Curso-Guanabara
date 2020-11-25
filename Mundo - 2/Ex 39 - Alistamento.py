import datetime

sexo=input('''Digite o sexo:
M - Masculino
F- Feminino\n''')
if(sexo=='M'):
    anonascimento = int(input('Digite o ano de nascimento:\n'))

    ano= datetime.date.today()

    idade = ano.year - anonascimento

    if(idade<18):
        print(f"O jovem ainda vai se alistar\nIdade atual: {idade}\n Faltam {18 - idade} anos")
    elif(idade == 18):
        print(f'Está na hora de se alistar\nIdade: {idade}')
    elif(idade>18):
        print(f'Já passou da hora de se alistar\nIdade: {idade}\nAtrasou {idade-18} anos')

else:
    print('não é obrigatorio o alistamento militar')