altura = float(input('Digite a altura:\n'))
peso = float(input('Digite o peso:\n'))

imc = peso/(altura**2)

if(imc<18.5):
    print('Abaixo do peso')
elif imc>=18.5 and imc<25:
    print('Peso ideial')
elif imc>=125 and imc<30:
    print('Sobrepeso')
elif imc>=30 and imc<40:
    print('Obesidade')
elif imc>=40:
    print('Obesidade mórbida')
