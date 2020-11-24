frase = input("Digite uma frase\n").lower()

qtdeA=frase.count('a')

priA=frase.index('a')
ultpalavra=frase.split()

ultA=frase.rfind('a')
print(f' quantidade de "a" na frase: {qtdeA}\nindice do primeiro "a": {priA+1}\nindice do ultimo "a": {ultA+1}')