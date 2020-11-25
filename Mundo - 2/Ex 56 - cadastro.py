hmais=''
idadeant=0
qtdemulher=0

for i in range(4):
    
    nome = input('Digite o nome:\n')
    s = input('''Digite o sexo: F- Feminino; M - Masculino\n''')
    idade = int(input('Digite a idade da pessoa:\n'))

    if (s=='M' and hmais==''):
        hmais = nome
        idadeant=idade
    
    elif(s=='M' and idade>idadeant ):
        hmais=nome
        idadeant = idade
    
    elif s=='F' and idade <20:
        qtdemulher+=1

print(f'''Nome do homem mais velho: {hmais}
Qtde de mulheres menores de 20 anos: {qtdemulher}''')

