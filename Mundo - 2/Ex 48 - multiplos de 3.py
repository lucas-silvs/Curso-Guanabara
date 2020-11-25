s=0
for i in range(0,500,3):
    if i%2!=0:
        s=s+i
        print(i)

print(f'soma de todo os impares multiplos de 3 entre 1 a 500: {s} ')