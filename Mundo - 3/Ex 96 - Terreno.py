def area(base,altura):
    area = base * altura
    print(f'A área do retangulo é igual a {area:.2f}m^2')


base=float(input('Digite o valor da base do retangulo:\n'))
altura = float(input('Digite o valor da altura do retangulo:\n'))

area(base,altura)