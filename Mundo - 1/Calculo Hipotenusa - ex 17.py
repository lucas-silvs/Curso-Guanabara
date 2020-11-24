import math as m 
cateto_oposto = float (input('Digite o valor do cateto oposto\n'))
cateto_adjacente = float (input('Digite o valor do cateto adjacente\n'))
hipotenusa = m.sqrt(pow(cateto_oposto,2) + pow(cateto_adjacente,2))

print(f'O valor da hipotenusa será {hipotenusa}')