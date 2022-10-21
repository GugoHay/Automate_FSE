import os
#Fonction pour supprimer ce qu'il y as après le F dans une liste
def sortList(listName):
    listNameStr = str(listName[0])                          #On transforme notre liste en string
    listNameSplit = listNameStr.split("/",-1)               #On retire le/les "/" après le F et on rajoute des indexs dans notre liste

    while len(listNameSplit) > 1:                           #Tant que l'index de notre liste est plus grand que 1
        listNameSplit.pop(-1)                               #On retire de la liste le dernier index
    if len(listNameSplit) == 1 :                            #Si la longueur de notre liste est égal à 1 (donc un seul index)
        listNameSplit.append("\n")                          #On ajoute simplement le saut de ligne en tant que nouvelle index
        w = "".join(listNameSplit)                          #On joint ensuite les deux index pour en faire qu'un (c'est simplement pour avoir le saut de ligne à la fin)
    return w


#Fonction de recupération de la liste RegroupFSE
def getLineOfRegroup(fileName):
    word = "RegroupFSE="                                    #Variable du mot pour trouver la ligne            RegroupFSE=xxxxxxxxxx          F
    with open(fileName, 'r+') as f:                         #On ouvre le fichier en mode "lecture/écriture"
        f_lines = f.readlines()                             #On lis chaque ligne du fichier
        ls_lines = []                                       #Liste vide, qui comportera la ligne que l'on souhaite modifier dans la suite du code
        for line in f_lines :                               #Pour chaque ligne dans f_lines
            if line.find(word) != -1:                       #Si on trouve le mot souhaité dans la ligne
                ls_lines.append(line)                       #Ajoute la ligne qui comporte le mot dans ma liste ls_line
    sortList(ls_lines)                                      #On initie la fonction sortList pour "épurée" notre liste 'ls_lines'
    f.close()


#A Travailler
# def getLineToReplace(fileName):
#     word = "ErreurFSE=A"
#     with open(fileName, 'r+') as f:
#         f_lines = f.readlines()
#         total_lines = len(f_lines)
#         for line in f_lines :
#             if line.startswith(word):
#                 index = f_lines.index(word + "\n")
#                 f_lines.pop(index)
#                 print(f_lines)
#                 with open(fileName, 'w') as fw:
#                     strOff_lines = str(f_lines)
#                     f.write(strOff_lines)
#     f.close()

# getLineToReplace("FseUnlocker\File000009322.hif")

def getLinesFromFile(fileName):
    toClean = ["ErreurFSE=","RemissionFSE=","DansFSE=","EnvoiFSE=","ErreurFSE=","Incident="]
    input = open(fileName, 'r')
    output = open("x.txt", 'w')
    with input as f:
        for line in f:
            if "ErreurFSE=A" in line:
                print("x")
            else:
                with output as f1:
                        if "ErreurFSE=A" in line:
                            f1.write(line)


getLinesFromFile("FseUnlocker/File000009300.hif")