from time import sleep

 
def manual(comando=''):
    print(f'\033[1;94;107m')
    help(comando)
    print(f'\033[m')

    
    


c='s'

while c == 's':
    sis=   'SISTEMA DE AJUDA PyHELP'
    print(f'\033[1;97;102m{(len(sis)+4)*"~"}\033[m')
    print(f'\033[1;97;102m  {sis}  \033[m')
    print(f'\033[1;97;102m{(len(sis)+4)*"~"}\033[m')

    comando = input('Qual comando deseja consultar:\n')
    print(f'\033[1;94;107m{(len(f"Consultando o código {comando}  ")+4)*"-"}\033[m')
    print(f'\033[1;94;107m  Consultando o código "{comando}"\033[m')
    print(f'\033[1;94;107m{(len(f"Consultando o código {comando}  ")+4)*"-"}\033[m')
    sleep(2)
    man=str(manual(comando))

    
    


    c = input('Deseja Continuar: [S/N]\n ')
