from socket import *
import numpy as np

#funcao que traduz a palavra "word" para a lingua desejada
def translate (word, language_1, language_2):
    #traduz "word" da "language1" para a "language2"

    dic = open('dictionary.txt', 'r')
    if language_1 == "en":
        l1 = 0
    elif language_1 == "pt":
        l1 = 1
    elif language_1 == "fr":
        l1 = 2

    if language_2 == "en":
        l2 = 0
    elif language_2 == "pt":
        l2 = 1
    elif language_2 == "fr":
        l2 = 2

    en = []
    pt = []
    fr = []
    for line in dic:
        colunas = line.split() #separa as linhas do arquivo
        en.append(colunas[0]) #lista com palavras em ingles
        pt.append(colunas[1])
        fr.append(colunas[2])

    matrix = np.array([en,pt,fr])

    position = 0
    w = word
    if w in matrix[l1]:
        for position, name in enumerate(matrix[l1]):
            if name == w:
                p = position
                break

    else:
        notFound = 1
        return notFound
    
    return matrix[l2][p]
#fim "translate"

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind ( ('', 1234) )
serverSocket.listen(1)

print ('Servidor pronto')

while 1:
    connectionSocket, addr = serverSocket.accept()
    palavra = connectionSocket.recv(1024).decode()
    print(palavra)
    l1 = connectionSocket.recv(1024).decode()
    print(l1)
    l2 = connectionSocket.recv(1024).decode()
    traducao = translate(palavra, l1, l2)
    connectionSocket.send(traducao.encode())
    connectionSocket.close()