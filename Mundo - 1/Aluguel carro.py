qtdekm=float(input('Digite a quantidade de Km percorridos\n'))
dias= int(input('digite a quantidade de dias alugados\n'))

valor = (dias * 60) + (qtdekm * 0.15)

print(f' o valor final do aluguel será de R$ {valor}')