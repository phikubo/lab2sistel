import socket

def main():
	host='192.168.4.1'
	port=3031

	s=socket.socket()
	s.connect((host,port))

	message=raw_input("-->rwinpt")
	while message!='q':

		s.send(message.encode())
		data=s.recv(1024).decode()

		print("Recibido del servidor",str(data))
		message=raw_input("--->")

	s.close()

if __name__ == '__main__':
	main()