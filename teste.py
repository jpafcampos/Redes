def translate (word, language_1, language_2)
    dic = open('dictionary.txt', 'r')
    if language_1 == "en":
        l1 = 0
    elif language_1 == "pt":
        l1 = 1
    elif language_1 == "fr"
        l1 = 2

    if language_2 == "en":
        l2 = 0
    elif language_2 == "pt":
        l2 = 1
    elif language_2 == "fr"
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




inf = open('dictionary.txt','r')
en = []
pt = []

for line in inf:
    parts = line.split()
    en.append(parts[0])
    pt.append(parts[1])

matrix = np.array([en,pt])
print(matrix[0][1])

position = 0
word = "cat"   
if word in matrix[0]:
    for position, name in enumerate(matrix[0]):
        if name == word:
            print("Your word is in the list at ", position)
            p = position
            position = 1000
else:
    print('Your word is not in the sentence')