import socket

def main():
	host='192.168.4.1'
	port=3030

	s=socket.socket()
	s.connect((host,port))

	message='d'
	while message!='q':
    #print("entro")
		s.send(message.encode())
		data=s.recv(1024).decode()

		print("Recibido del servidor",str(data))
		message=raw_input("--->")

	s.close()

if __name__ == '__main__':
	main()
