import math as m
angulo=float(input('Digite o valor do angulo\n'))
angulo = m.radians(angulo)
seno = m.sin(angulo)
cosseno= m.cos(angulo)
tangente = m.ceil(m.tan(angulo))

print(f'Seno: {seno:.2f}, Cosseno: {cosseno:.2f} e a Tangente: {tangente} do angulo digitado')