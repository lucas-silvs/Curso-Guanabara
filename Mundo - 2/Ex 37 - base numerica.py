num= int(input('Digite um número:\n'))

choice = int(input("Escolha uma base de conversão\n1-binário\n2-octal\n3-hexadecimal:\n"))

if(choice==1):
    b=bin(num)[2:]
    print(f'O Número {num} convertido para binário ficara: {b}')


elif(choice==2):

    print(f'O Número {num} convertido para binário ficara: {oct(num)[2:]}')

elif (choice == 3):

    print(f'O Número {num} convertido para binário ficara: {hex(num)[2:]}')
     

