frase = input('Digite uma frase:\n').lower()
frase = frase.replace(" ","")

fraser=''
for i in range(len(frase)-1,-1,-1):
    fraser=fraser+frase[i]

if(frase == fraser):
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')