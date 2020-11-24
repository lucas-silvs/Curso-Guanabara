a = float(input('Dige o tamanho do segmento de reta:\n'))
b = float(input('Dige o tamanho do segmento de reta:\n'))
c = float(input('Dige o tamanho do segmento de reta:\n'))

if( ( a>(abs (b-c) ) and a< b+c )  or ( b>(abs (a-c) ) and b< a+c ) or ( c>(abs (a-b) ) and c< a+b )):
    print("As retas forma um triângulo")
else:
    print('As retas não forma um triângulo')
