def leiaDinheiro(texto):
    din=''
    c=0
    while c==0:
        din = input(texto)
        if ',' in din:
           din =  din.replace(',','.')
        try:
            float(din)
            c=1
        except:
            print('Digite um valor número valido\n')
      
    

    f = float(din)

    return f

