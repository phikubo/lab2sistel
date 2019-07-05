#implemented by phikubo

#a este modulo se le llama desde otro modulo asi:
#conetar_red.main()
def main():
    import network
    import time
    import socket
    host="192.168.4.1"
    port=3000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((host,port))
    message=""
    while message != 'bye':
        print("while")
        #s.send(message.encode())
        data = s.recv(1024).decode()
        print("Received from server: ", str(data))
        #message = input("-->")
        message=str(data)
        print(message)
        #s.send(message.encode())
    print("cerrando socket")
    s.close()
        
if __name__ == '__main__':
    main()
else:
    print('Modulo Conectar_red importado')



