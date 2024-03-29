# Author: Gurguen Sahakian
# Create random FSE

import random
from turtle import clear


# pour chaque index dans myList .append une autre liste qui sera transformer grâce à join en str en plus d'ajouter un '+' entre chaque valeur
mylist = []
ccam = ["QZLA004","QZGA002","JKLD001","JKKD001","JKHD001","JNQM001","JQQM010","JQQM015","JQQM018","JQQM019","JQQM016","JQQM017","JQQJ037","ZCQJ001","ZCQJ002","ZCQJ003","ZCQJ006","ZCQM003","JQGD010","JQGD012","JQGD004","JQGD001","JQGD003","JQGD008","JQGD002","JQGD007","QZRB001"]

# Montant honoraire
hono = []
# Neant
listdepen = []
# 1 
listquant = []
listcoef = []
# 10 
listcompl = []
# ___
listmodif = []
listsuppl = []
# N
listdomic = []
listdjf = []
listurgen = []
listnuit = []

#Fonction d'ajout de prix au format str selon le nombre d'index dans la liste "myList".
def ajout_hono(laListe):
    for p in mylist:
        #permet d'attribuer un prix entre deux valeurs
        #laListe.append(str(random.randint(473,999)))

        # "?" permet à pyx d'assigner le prix de base secu automatiquement
        laListe.append("?")

#Fonction d'ajout de caractère selon le nombre d'index dans la liste "myList".
def ajout_neant(laListe):
    for p in mylist:
        laListe.append("Néant")

def ajout_trait(laListe):
    for p in mylist:
        laListe.append("___")

def ajout_coeff(laListe):
    for p in mylist:
        laListe.append("1")

def ajout_uino(laListe):
    for p in mylist:
        laListe.append("N")

def ajout_compl(laListe):
    for p in mylist:
        laListe.append("10")

#Fonction de creation flux actes
def filecreator():
    
    global mylist
    global listdepen
    global listmodif
    global listsuppl
    global listquant
    global listcoef
    global listdomic
    global listdjf
    global listurgen
    global listnuit
    global listcompl
    global hono
   
    nbMin = 1
    nbMax = 5
    while nbMin < nbMax :
        z = random.randint(1,20)
        mylist = random.sample(ccam, z)
        #Dans cette partie on incrémente grâce au fonction ajout_ les caractères pour chaque index de mylist (à modifier, car on peut simplifier)
        ajout_neant(listdepen)
        ajout_trait(listmodif)
        ajout_trait(listsuppl)
        ajout_coeff(listquant)
        ajout_coeff(listcoef)
        ajout_uino(listdomic)
        ajout_uino(listdjf)
        ajout_uino(listurgen)
        ajout_uino(listnuit)
        ajout_compl(listcompl)
        ajout_hono(hono)
        #Creation de fichier .hif avec le suivie des numéro de fse
            #with open(f"FSE{str(x).zfill(9)}.hif","w") as f:
        #Creation de fichier .par pour les flux actes_.par
        with open(f"CVActes_{str(nbMin).zfill(9)}.par","w") as f:    
            
            beneficiaire_txt = f"""
[Beneficiaire]
Nom=AIMETE
Prenom=VINCENT
Date_de_naissance=17/11/1988
Rang_gemellaire=1
Qualite=Assuré

[Assure]
Numero=1881134170052
Cle=26

[Medico_administratif]
Code_regime=01
Caisse_gestionnaire=349
Centre_gestionnaire=9881

"""
            iris = f"""
[IRIS]
Nature_piece_justificative=0
Date=05/04/2022

"""
            amc = f"""
[AMC]
Gestion=S
Attestation=O
Organisme=1100000000
Date1=01/01/2000
Date2=01/01/2099
Traitement=33
Formule=052$0

"""
            prescription = f"""
[Prescription]
Date=14/11/2020
Numero=99100010
Cle=0
Code_specialite=01

"""
            assu = f"""
[Assurance]
Nature=10
Accident=N
Alsace_Moselle=N

"""
            rembou = f"""
[Remboursement]
Tiers_payant_partie_obligatoire=O
AMC=N
Tiers_payant_partie_complémentaire=O
Medecin_SNCF=N

"""
#Ici la variable txt, prend en compte les listes et les transformes en string avec une séparation pour chaque valeur dans les listes
            txt = f"""
[PRESTATION]
Quantite={str(("+").join(listquant))}
Coefficient={str(("+").join(listquant))}
Code_CCAM={str(("+").join(mylist))}
Code_compl_CCAM={str(("+").join(listcompl))}
Modificateurs_CCAM={str(("+").join(listmodif))}
Code_suppl_CCAM={str(("+").join(listsuppl))}
Code_affine=
Qualificatif_depense={str(("+").join(listdepen))}
Domicile={str(("+").join(listdomic))}
D_jf={str(("+").join(listdjf))}
Nuit={str(("+").join(listnuit))}
Urgence={str(("+").join(listurgen))}
Code=
Montant_honoraires={str(("+").join(hono))}
"""
            f.write(beneficiaire_txt + iris + amc + prescription + assu + rembou + txt)
            f.close()
        #une fois notre fichier écrit, on clear les listes pour repartir à zéro car on reste dans la boucle tant que x > y.
            mylist.clear()
            listdepen.clear()
            listcoef.clear()
            listcompl.clear()
            listdjf.clear()
            listdomic.clear()
            listmodif.clear()
            listnuit.clear()
            listquant.clear()
            listsuppl.clear()
            listurgen.clear()
            hono.clear()
        #On incrémente de 1 la valeur de x pour éviter la boucle infini
            nbMin = nbMin + 1


#Lancement de ma fonction de creation flux actes
filecreator()
