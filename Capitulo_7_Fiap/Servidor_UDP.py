from socket import *

servidor = '127.0.0.1'
porta = 43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((servidor, porta))
print('Servidor UDP pronto pra uso.....')

while True:
    dados, origem = obj_socket.recvfrom(65535)
    print('Origen .................: ', origem)
    print('Dados recebidos: ', dados.decode())
    resposta = input('Digite a sua resposta: ')
    obj_socket.sendto(resposta.encode(), origem)
obj_socket.close()
