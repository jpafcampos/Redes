#encoding:utf-8
from socket import *
import numpy as np

#funcao que traduz a palavra "word" para a lingua desejada
def translate (word, language_1, language_2):
    #traduz "word" da "language1" para a "language2"
    word = word.lower()
    dic = open('dicio2.txt', 'r', encoding = "utf8")
    if language_1 == "en":
        l1 = 0
    elif language_1 == "pt":
        l1 = 1
    elif language_1 == "fr":
        l1 = 2
    elif language_1 == "es":
        l1 = 3
    elif language_1 == "it":
        l1 = 4
    elif language_1 == "de":
        l1 = 5
    elif language_1 == "zu":
        l1 = 6
    elif language_1 == "eo":
        l1 = 7

    if language_2 == "en":
        l2 = 0
    elif language_2 == "pt":
        l2 = 1
    elif language_2 == "fr":
        l2 = 2
    elif language_2 == "es":
        l2 = 3
    elif language_2 == "it":
        l2 = 4
    elif language_2 == "de":
        l2 = 5
    elif language_2 == "zu":
        l2 = 6
    elif language_2 == "eo":
        l2 = 7

    en = []
    pt = []
    fr = []
    es = []
    it = []
    de = []
    zu = []
    eo = []

    for line in dic:
        colunas = line.split() #separa as linhas do arquivo
        en.append(colunas[0]) #lista com palavras em ingles
        pt.append(colunas[1]) #pt
        fr.append(colunas[2]) #fr
        es.append(colunas[3]) #es
        it.append(colunas[4]) #it
        de.append(colunas[5]) #de
        zu.append(colunas[6]) #zu
        eo.append(colunas[7]) #eo

    matrix = np.array([en,pt,fr, es, it, de, zu, eo])

    #print(matrix)
    position = 0

    indice = list(matrix[l1]).index(word) if word in matrix[l1] else -1
    if indice == -1:
        print(indice)
        return "erro"

    traducao = matrix[l2][indice]
    return traducao

    '''
    print(w)
    if w in matrix[l1]:
        print(w)
        for position, name in enumerate(matrix[l1]):
            if name == w:
                p = position
                break

    else:
        notFound = 1
        return 'Palavra não encontrada. Tente novamente.'
        print(matrix[l2][p])
    
    return matrix[l2][p]
'''
#fim "translate"

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind ( ('172.22.121.100', 8888) )
#serverSocket.bind ( ('', 12007) )
serverSocket.listen(1)

print ('Servidor pronto')

fim = 0
connectionSocket, addr = serverSocket.accept()
while fim == 0:
    palavra = connectionSocket.recv(1024).decode()
    print(palavra)
    l1 = connectionSocket.recv(1024).decode()
    print(l1)
    l2 = connectionSocket.recv(1024).decode()
    print(l2)
    
    traducao = translate(palavra, l1, l2)
    print(traducao)
    connectionSocket.send(traducao.encode())
    print('sent')
    ans = connectionSocket.recv(1024).decode()
    if ans == "n":
        fim = 1
        connectionSocket.close()
