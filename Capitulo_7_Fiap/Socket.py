import socket

resp = 'S'

while resp == 'S':
    url = input('Digite uma URL:\n')
    ip = socket.gethostbyname(url)
    print(f'P IP da url informada é: {ip}')
    resp = input('Digite "s" caso queira continuar:\n').upper()
