def aumentar(f,a,formatado = False):
    af = f+ (f * a/100)
    if formatado == True:
        af = moeda(af)

    return af


def diminuir(f,d,formatado = False):
    df = f - (f * d/100)

    if formatado == True:
        df = moeda(df)

    return df


def dobro(f,formatado = False):

    dof = f * 2

    if formatado == True:
        dof = moeda(dof)


    return dof


def metade(f,formatado = False):

    mf = f/2

    if formatado == True:
        mf = moeda(mf)


    return mf


def moeda(r):
    reais = f'R$ {r:.2f}'
    return(reais)


def resumo( f):

    print(f'''
    Valor analisado: {moeda(f)}
    Dobro do preço: {dobro(f,True)}
    Metade do preço: {metade(f,True)}
    80% de aumento: {aumentar(f,80,True)}
    35% de aumento: {diminuir(f,35,True)}''')


