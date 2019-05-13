from socket import *

serverName = 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect( ('', 1234) )
palavra = input('Digite uma palavra:')
clientSocket.send(palavra.encode())
l1 = input('Indique o idioma de origem: (en, fr, pt)' )
clientSocket.send(l1.encode())
l2 = input('Indique o idioma destino:')
clientSocket.send(l2.encode())
traducao = clientSocket.recv(1024).decode()

print ('Tradução:', traducao)

clientSocket.close()