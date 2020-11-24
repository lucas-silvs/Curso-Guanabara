salario = float(input('Digite o salário:\n'))
aumento=0
if salario > 1250.00:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15
print(f'O aumento será de R${salario+aumento:.2f}')