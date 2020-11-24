a = float(input('Dige o tamanho do segmento de reta:\n'))
b = float(input('Dige o tamanho do segmento de reta:\n'))
c = float(input('Dige o tamanho do segmento de reta:\n'))

if( ( a>(abs (b-c) ) and a< b+c )  or ( b>(abs (a-c) ) and b< a+c ) or ( c>(abs (a-b) ) and c< a+b )):
    print("\033[0;34;40m As retas forma um triângulo\033[m")
else:
    print('\033[4;33;40m As retas não forma um triângulo\033[m')
