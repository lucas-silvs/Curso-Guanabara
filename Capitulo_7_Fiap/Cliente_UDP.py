from socket import  *
servidor = '127.0.0.1'
porta = 43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
saida = ''

while saida !='X':
    msg = input('Digite sua mensagem:\n')
    obj_socket.sendto(msg.encode(),(servidor,porta))
    dados, origem = obj_socket.recvfrom(65535)
    print('Resposta do servidor: ',dados.decode())
    saida = input('Digite "X" para sair: ').upper()