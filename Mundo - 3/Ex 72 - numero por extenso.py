num=('zero','um','dois','três','quatro','cinco', 'seis', 'sete','oito', 'nove', 'dez', 'onze', 'doze', 'treze','catorze','quinze','dezesseis', 'dezesete','dezoito','dezenove','vinte')


n=int(input('Digite um número de 0 a 20:\n'))

while n<0 or n>20:
    n=int(input('Digite um número de 0 a 20:\n'))

print(f'O número que tu digitou é: {num[n]}')