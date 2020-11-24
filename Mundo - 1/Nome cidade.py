nome = input("Digite o nome de uma cidade:\n").lower().split()
e=nome[0].find("santo")

print(f'Resultado: {e}\nSe for igual a 0, o nome começa com Santo, senão, não começa com a palavra Santo')
