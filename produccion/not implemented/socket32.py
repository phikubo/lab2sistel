#implemented by phikubo

#a este modulo se le llama desde otro modulo asi:
#conetar_red.main()
def main():
    import network
    import time
    import socket
    import gc
    host="192.168.4.1"
    puerto=3000

    addr_server = socket.getaddrinfo(host, puerto)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr_server)
    time.sleep(0.3)
    print("Sever Address: ", addr_server)
    s.listen(2)
    c, addr_client = s.accept()
    time.sleep(0.3)
    print("c: ",c)
    print("addr ",addr_client)
    gc.collect()

    msg="Iteracion"
    counter=0
    message=msg+str(counter)
    print("ok1")
    time.sleep(0.5)
    while message != 'bye':
        print("ok2")
        if counter==10:
            message="bye"
        counter=counter+1
        s.send(message.encode())
        print(counter)
        #data = s.recv(1024).decode()
        #print("Received from server: ", str(data))
        #message = input("-->")
        #message=str(data)
        #s.send(message.encode())
        
    print("cerrando socket")
    s.close()
        
if __name__ == '__main__':
    main()
else:
    print('Modulo Conectar_red importado')


'''
    def __init__(self,puerto):
        #variables
        self.puerto=puerto
        self.host='192.168.4.1'
        self.id='zona 1'
        
    def iniciar_socket(self):
        self.addr_server = socket.getaddrinfo(self.host, self.puerto)[0][-1]
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(self.addr_server)
        time.sleep(0.3)
        print("Sever Address: ", self.addr_server)
        self.s.listen(2)
        self.c, self.addr_client = self.s.accept()
        time.sleep(0.3)
        print("c: ",self.c)
        print("addr ",self.addr_client)
        gc.collect()
    def funciones(self):
        pass
    def responder(self):
        time.sleep(0.2)
        print("servidor respondera 200")
        self.data_resp="200"
        self.c.send(self.data_resp.encode())

'''
