#Autor : Gurguen Sahakian
#Description : Générateur de flux CVActes

# Import des modules
import random


# Import des fichiers externes / dictionnaires
from benef_dict import *
from iris_dict import *
from amc_dict import *
from prescription_dict import *
from remboursement_dict import *
from prestation_dict import *

def actes_gen(nbMax):
    
    nbMin = 1   #Ce chiffre peut être modifier / si vous souhaitez générer des actes à partir du numéro 522 par exemple, remplacer par 522
                #Dans ce cas la valeur de nbMax sera forcement plus grand ou égal à 522
    while nbMin < nbMax :
        # Crée un nouveau fichier .par avec comme nom "CVActes_" puis le numéro de facture ".par"
        with open(f"CVActes_{str(nbMin).zfill(9)}.par","w") as f:

            compteur_dict = {'compteur':f"""[Facture]\nNumero={str(nbMin).zfill(9)}"""} #Dictionnaire du compteur
            # Choisi aléatoirement une clé dans un dictionnaire afin de l'écrire
            f.write(
                    (random.choice(list(benef_dict.values())))          +   #Dictionnaire des bénéficiaires
                    (random.choice(list(iris_dict.values())))           +   #Dictionnaire IRIS
                    (random.choice(list(amc_dict.values())))            +   #Dictionnaire des AMC
                    (random.choice(list(prescription_dict.values())))   +   #Dictionnaire des prescripteurs
                    (random.choice(list(remboursement_dict.values())))  +   #Dictionnaire des remboursements
                    (random.choice(list(prestation_dict.values())))     +   #Dictionnaire des remboursements
                    (random.choice(list(compteur_dict.values())))           #Dictionnaire du compteur (celui-ci n'est pas dans un fichier à part)
                    )
            
            f.close() #Ferme le fichier à la fin de l'écriture
            
            nbMin += 1 #Incrémentation de 1 de nbMin afin d'éviter la boucle infinie

actes_gen(50)   #Modifier le chiffre par le nombre factures que vous voulez générer.


