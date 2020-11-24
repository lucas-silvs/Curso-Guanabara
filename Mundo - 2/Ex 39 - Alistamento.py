import datetime
anonascimento = int(input('Digite o ano de nascimento:\n'))

ano= datetime.date.today()

idade = ano.year - anonascimento

if(idade<17):
    print(f"O jovem ainda vai se alistar\nIdade atual: {idade}\n Faltam {17 - idade} anos")
elif(idade == 17):
    print(f'Está na hora de se alistar\nIdade: {idade}')
elif(idade>17):
    print(f'Já passou da hora de se alistar\nIdade: {idade}\nAtrasou {idade-17} anos')
