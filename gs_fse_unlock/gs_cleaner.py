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
from tkinter import messagebox
# All files and directories ending with .txt and that don't begin with a dot:
#print(glob.glob("*.hif")) 
# All files and directories ending with .txt with depth of 2 folders, ignoring names beginning with a dot:
#print(glob.glob("/home/adam/*/*.hif")) 

#Liste mes fichiers .hif et .fs dans de liste respectivement
dir_hif_list = glob.glob("*.hif")
dir_fs_list = glob.glob("*.fs_")
dir_fse_list = glob.glob("*.fse")

dir_loc = os.getcwd()
isdir_temp = os.path.isdir(dir_loc + "/temp")


def GCleaner():
    dirName = "temp"
    

    if not isdir_temp:
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
            docList_g = []
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
                for x in docList_f:
                    if not str(x).find("RetourFSE="):
                        lreplace = x.replace(x,"")
                        docList_g.append(lreplace)
                    else:
                        docList_g.append(x)
                    #------------------------------ 
                    #Retire les caractère apres le F (retire la ligne de la liste, modifie la ligne et la ré-implémente dans le liste.)   
                for x in docList_g:
                    if "RegroupFSE=" in x :
                        st = slice(51)
                        sti = x[st]
                        docList_g.pop(docList_g.index(x))
                        docList_g.insert(5,sti)
                    #Retire les informations inutile dans infos (après le petit -)
                for x in docList_g:
                    if "Info=" in x :
                        info_list = x
                        cuted_tuple = info_list.partition("-")
                        ls_cuted = list(cuted_tuple)
                        del ls_cuted[-1] #retire le dernier element du tuple (apres le -)
                        docList_g.pop(docList_g.index(x))
                        str_ls_cuted = "".join(ls_cuted)
                        docList_g.insert(7,str(str_ls_cuted))
                cleaned = True
            else:
                cleaned = False
                print("ErreurFSE=A est présent dans ce fichier. Traitement manuel")
            if cleaned == True :
                outPath = r"temp/"
                #Les fichiers .hif et .fs_ sont encodé en ANSI
                with open(outPath + str(files), "w", encoding="ANSI") as f:
                    for i in docList_g:
                        f.write(i)
                        f.write("\n")

                fst = slice(13)
                fsti = str(files[fst]) #str du nom de fichier
                fsti_fs = str(fsti) + ".fs_"
                fsti_fse = str(fsti) + ".fse"
                # fsti_fs_dir = os.path.isdir(dir_loc + '/' + fsti_fs )
                # fsti_fs_in_temp_dir = os.path.isdir(dir_loc + "/temp/" + fsti_fs)

                if fsti_fs in dir_fs_list:
                    shutil.move(fsti_fs, outPath)
                    os.rename(outPath + fsti_fs, outPath + fsti_fse) #renomme les .fs_ en .fse  
                else :
                    pass

                if fsti_fse in dir_fse_list:
                    pass
                
            else :
                print("le fichier n'as pas était modifier")
                continue
        messagebox.showinfo("FSE UNLOCKER","Fin du processus, les fichiers ont été correctement nettoyer")
    else:
        messagebox.showinfo("FSE UNLOCKER","Merci de supprimer le dossier 'temp' existant.")
    
    
GCleaner()
