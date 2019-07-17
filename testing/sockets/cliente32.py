import socket

def main():
	to_host='192.168.4.1'
	to_port=3031

	s=socket.socket()
	s.connect((host,port))

	message="Saludos..."
	s.send(message.encode())
	#data=s.recv(1024).decode()
	msg="Msg 1"
	time.sleep(2)
	s.send(msg.encode())
	msg="Msg 2"
	time.sleep(2)
	s.send(msg.encode())
	
		

	s.close()

if __name__ == '__main__':
	main()
