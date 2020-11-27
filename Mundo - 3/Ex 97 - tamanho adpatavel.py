def escreva(pal):

    tam=len(pal)+2

    print(tam * '~')
    print(f' {pal}')
    print(tam * '~')

p = input('Digite uma palavra:\n')
escreva(p)