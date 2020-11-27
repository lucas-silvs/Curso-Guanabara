def leiaint(n):
    num=''
    while num.isnumeric()==False:
        num=input(n)
        print ('O texto digitado não é um número')
    
    return f'Você acabou de digitar o numero {num}'

j=leiaint('Digite um  número\n')

print(j)


