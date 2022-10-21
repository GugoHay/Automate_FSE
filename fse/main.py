
def Cleaner(inPath):
    docList = []
    with open(inPath, "r") as document:
        for line in document.readlines():
            docList.append(line)
    
    docList_a = []
    docList_b = []
    docList_c = []
    docList_d = []
    docList_e = []
    docList_f = []

    #Retire les sauts de ligne dans la liste    
    for x in docList:
        lreplace = x.replace("\n","")
        docList_a.append(lreplace)
    

    for x in docList_a:
        if not str(x).find("ErreurFSE=A"):
            print("ErreurFSE=A présent dans le document")
            break
        elif not str(x).find("ErreurFSE="): 
            lreplace = x.replace(x,"")
            docList_b.append(lreplace)
        else:
            docList_b.append(x)
        #------------------------------
    for x in docList_b:
        if not str(x).find("DansFSE="):
            lreplace = x.replace(x,"")
            docList_c.append(lreplace)
        else:
            docList_c.append(x)
        #------------------------------
    for x in docList_c:
        if not str(x).find("EnvoiFSE="):
            lreplace = x.replace(x,"")
            docList_d.append(lreplace)
        else:
            docList_d.append(x)
        #------------------------------
    for x in docList_d:
        if not str(x).find("Incident="):
            lreplace = x.replace(x,"")
            docList_e.append(lreplace)
        else:
            docList_e.append(x)
        #------------------------------
    for x in docList_e:
        if not str(x).find("RemissionFSE="):
            lreplace = x.replace(x,"")
            docList_f.append(lreplace)
        else:
            docList_f.append(x)

    print(docList_f)
Cleaner("File000009300.hif")