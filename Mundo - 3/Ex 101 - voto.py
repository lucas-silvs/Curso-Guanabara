from datetime import date
def voto(ano):
    anoatual= date.today().year
    idade = anoatual - ano 
    voto=''


    if idade>=18 and idade<70:
        voto='O voto é obrigatório'
    elif idade == 17 or idade>=70:
        voto='voto é opcional'
    elif idade<17:
        voto='Não vota'
    return voto


i= int(input('Digite o ano de nascimento:\n'))

print(voto(i))