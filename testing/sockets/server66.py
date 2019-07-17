import socket

def main():
	local_host='192.168.1.12'
	local_port=3333
	addr_server=socket.getaddrinfo(local_host,local_port)[0][-1]
	print('Addr_server: ',addr_server)
	s=socket.socket()
	s.bind(addr_server)
	print("server adrres",addr_server)
	s.listen(1)
	#Esperando por un cliente.
	c,addr_client=s.accept()
	print("client addres: ",str(addr_client))
	cc=0
	flag=True
	while flag==True:
		data=c.recv(1024).decode()
		print("Cliente dice: ",str(data))
		#data="To client: ok"#+str(data)
		#print("Servidor envia: ", str(data))
		#c.send(data.encode())
		time.sleep(2)
		if cc==10:
			flag=False
		cc=cc+1
	c.close




if __name__ == '__main__':
	main()
	#considerar hacer esto cada tantos segundos, o hacerlo while true

