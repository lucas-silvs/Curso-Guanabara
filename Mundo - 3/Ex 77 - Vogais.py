t=('alo','Lucas', 'da', 'Silva', 'Santos')


percorer=1
while percorer<=len(t):
    
    for i in t:
        vog=""
        if 'a' in i:
            vog+=" "+'a'
        if 'e' in i:
            vog+=" "+'e'
        if 'i' in i:
            vog+=" "+'i'
        if 'o' in i:
            vog+=" "+'o'
        if 'u' in i:
            vog+=" "+'u'
        print(f'na palavra: {i} tem as seguintes vogais: {vog}')
        percorer+=1




