#Autor : Gurguen Sahakian
#Description : Dévérouillage automatique des FSE en erreur.

# Fonction de cleaner qui prend en compte "ErreurFSE=A" si présent il n'éffectue aucune action, si non il néttoie le fichier et copie son contenue en mémoire dans un fichier à part.
# Il déplace le .fs_ dans le dossier temp et le renomme en .fse
# Seul les fichiers .fs_ sont déplacer, les .hif dans le dossier temp sont des fichiers comportant le même nom mais l'intérieur est clean.
# Il suffit de déplacer les fichiers temp dans le dossier courant pour que le deverouillage soit pris en compte.
# Les encodages sont pris en compte à la lecture et ecriture des nouveaux fichiers.

import glob
import shutil
import os
# All files and directories ending with .txt and that don't begin with a dot:
#print(glob.glob("*.hif")) 
# All files and directories ending with .txt with depth of 2 folders, ignoring names beginning with a dot:
#print(glob.glob("/home/adam/*/*.hif")) 

#Liste mes fichiers .hif et .fs dans de liste respectivement
dir_hif_list = glob.glob("*.hif")
dir_fs_list = glob.glob("*.fs_")

def GCleaner():
    dirName = "temp"
    os.mkdir(dirName)
    for files in dir_hif_list:
        docList = []
        #Les fichiers .hif et .fs_ sont encodé en ANSI
        with open(str(files), "r", encoding="ANSI") as document:
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
            cleaned = False
        if not "ErreurFSE=0" in docList_a: 
            for x in docList_a:
                if not str(x).find("ErreurFSE="): 
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
                if not str(x).find("Incident"):
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
                #------------------------------ 
                #Retire les caractère apres le F (retire la ligne de la liste, modifie la ligne et la ré-implémente dans le liste.)   
            for x in docList_f:
                if "RegroupFSE=" in x :
                    st = slice(51)
                    sti = x[st]
                    docList_f.pop(docList_f.index(x))
                    docList_f.insert(5,sti)
                    
            cleaned = True
        else:
            cleaned = False
            print("ErreurFSE=A est présent dans ce fichier. Traitement manuel")
        if cleaned == True :
            outPath = r"temp/"
            #Les fichiers .hif et .fs_ sont encodé en ANSI
            with open(outPath + str(files), "w", encoding="ANSI") as f:
                for i in docList_f:
                    f.write(i)
                    f.write("\n")

            fst = slice(13)
            fsti = str(files[fst])
            shutil.move(str(fsti) + ".fs_", outPath)
            fsName = fsti + ".fs_"
            #print(outPath + fsName)
            os.rename(outPath + fsName, outPath + fsti + ".fse")
        else :
            print("le fichier n'as pas était modifier")
            continue
GCleaner()
