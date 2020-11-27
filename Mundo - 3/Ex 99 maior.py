def maior(* num):
    maior = 0
    

    for i in num:
        print(i)
        for j in i:
            if i.index(j)==0:
                maior=int(j)
            elif int(j)>maior:
                maior = int(j)
    
    print(f'O maior valor digitado foi o : {maior}')


lista = input('Digite uma sequencia de número:\n').split()

lista = tuple(lista)


maior(lista)
   
        
        
