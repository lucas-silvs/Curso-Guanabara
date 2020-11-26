from random import randint
t=(randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100)) 


print(t)

t=sorted(t)

print(f'''
O menor número: {t[0]}
O maior número: {t[len(t)-1]}''')