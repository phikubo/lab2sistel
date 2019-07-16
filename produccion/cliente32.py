import socket

def main():
	host='192.168.4.1'
	port=3031

	s=socket.socket()
	s.connect((host,port))

	message="hola"
	while message!='q':

		s.send(message.encode())
		data=s.recv(1024).decode()

		print("Recibido del servidor",str(data))
		

	s.close()

if __name__ == '__main__':
	main()
