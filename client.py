from socket import *
import pickle
import sys

host = 'localhost'
port = 8081
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(addr)


print('Отправка матрицы...')

data = [
    [1,2],
    [3,4]
]
data = pickle.dumps(data)
tcp_socket.send(data)

data = pickle.loads(tcp_socket.recv(1024))
print('Пришел ответ:', data)


tcp_socket.close()
