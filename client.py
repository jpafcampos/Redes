from socket import *

serverName = 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect( ('192.168.0.14', 8888) ) 
#clientSocket.connect( ('', 1234) )

fim = 0;
while(fim == 0):
	palavra = input('Digite uma palavra:')
	clientSocket.send(palavra.encode())
	l1 = input('Indique o idioma de origem: (en, es, pt, fr, de, zu, eo, it) ' )
	clientSocket.send(l1.encode())
	l2 = input('Indique o idioma destino:')
	clientSocket.send(l2.encode())
	traducao = clientSocket.recv(1024).decode()
	print ('Tradução:', traducao)
	
	ans = input('Deseja continuar? (s/n) ')
	if(ans == "n"):
		fim = 1

	clientSocket.send(ans.encode())

clientSocket.close()