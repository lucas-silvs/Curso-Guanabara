valorcasa = float(input('Digite o valor da casa:\n'))
salario =float(input('Digite o salário:\n')) 
anos = int(input('Em quantos anos será pago\n'))

prest= valorcasa/(anos*12)

if prest>salario*0.30:
    print(f"Emprestimo negado, valor da prestaçã excede 30% a mais do salário\nsalario: {salario}\nprestação mensal: {prest}")
else:
    print(f'Emprestimo aprovado\nPrestação mensal: {prest}')