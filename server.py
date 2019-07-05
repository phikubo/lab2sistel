import socket

def main():
	host='192.168.4.1'
	port=3031
	addr_server=socket.getaddrinfo(host,port)[0][-1]
	print('Addr_server: ',addr_server)
	s=socket.socket()
	s.bind(addr_server)
	print("server adrres",addr_server)
	s.listen(1)

	c,addr_client=s.accept()
	print("client addres: ",str(addr_client))

	while True:
		data=c.recv(1024).decode()
		if not data:
			break
		print("Recibido desde el cliente: ",str(data))
		data=">>>"+str(data)
		print("sending to cliente: ",str(data))
		c.send(data.encode())
	c.close




if __name__ == '__main__':
	main()
	#considerar hacer esto cada tantos segundos, o hacerlo while true