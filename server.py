#Модуль socket для сетевого программирования
from socket import *
import pickle

#данные сервера
host = 'localhost'
port = 8081
addr = (host,port)

#socket - функция создания сокета 
#первый параметр socket_family может быть AF_INET или AF_UNIX
#второй параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
tcp_socket = socket(AF_INET, SOCK_STREAM)
#bind - связывает адрес и порт с сокетом
tcp_socket.bind(addr)
#listen - запускает прием TCP
tcp_socket.listen(100)

#Бесконечный цикл работы программы
while True:
   
    print('Ожидание подключения...')
    
    #accept - принимает запрос и устанавливает соединение, (по умолчанию работает в блокирующем режиме)
    #устанавливает новый сокет соединения в переменную conn и адрес клиента в переменную addr
    conn, addr = tcp_socket.accept()
    print('client: ', addr)
    
    #recv - получает сообщение TCP
    data = list(pickle.loads(conn.recv(1024)))
    #если ничего не прислали, завершим программу
    if not data:
        conn.close()
        break
    else:
        print('Исходная матрица:', data)
        det = int(int(data[0][0]) * int(data[1][1]) - int(data[0][1]) * int(data[1][0]))
        print('det A:', det)

        data = [[el * det for el in line] for line in data]

        print('Умноженная Матрица:', data)
        #send - передает сообщение TCP
        conn.send(pickle.dumps(data))
        #close - закрывает сокет
        conn.close()
    
    #Если мы захотели выйти из программы
    question = input('Выйти? 1\\0: ')
    if question == '1': break
    
tcp_socket.close()
