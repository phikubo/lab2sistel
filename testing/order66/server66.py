
import socket
import time
import ondas66
import plotear66
def main_sock():
	host='192.168.1.15'
	port=3032
	addr_server=socket.getaddrinfo(host,port)[0][-1]
	print('Addr_server: ',addr_server)
	s=socket.socket()
	s.bind(addr_server)
	print("server adrres",addr_server)
	s.listen(1)

	c,addr_client=s.accept()
	print("client addres: ",str(addr_client))
	cc=0
	flag=True
	while flag==True:
		data=c.recv(1024).decode()
		print("Cliente dice: ",str(data))
		if data:
			dato=data.split()
			tipo1=int(dato[0])
			tipo2=int(dato[1])
			amplitud=int(dato[2])
			w0=float(dato[3])
			phi1=float(dato[4])
			phi2=float(dato[5])
			k=5
			w0=0.09
			max=84
			puntos=84
			try:
				dato1=ondas66.pltwave(max, puntos, k, amplitud, w0, phi1, tipo1)
				dato2=ondas66.pltwave(max, puntos, k, amplitud, w0, phi2, tipo2)
				plotear66.plot(dato1, dato2)
			except Exception as e:
				print(e)
		if cc==2:
			flag=False
		cc=cc+1
	c.close




if __name__ == '__main__':
	main_sock()
	#considerar hacer esto cada tantos segundos, o hacerlo while true




