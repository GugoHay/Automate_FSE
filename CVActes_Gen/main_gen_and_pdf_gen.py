#Autor : Gurguen Sahakian
#Description : Générateur de flux CVActes & PDF en parallèle

# Import des modules
import random
from fpdf import FPDF



# Import des fichiers externes / dictionnaires
from benef_dict import *
from iris_dict import *
from amc_dict import *
from prescription_dict import *
from remboursement_dict import *
from prestation_dict import *


# Fonction de génération de FSE en prenant en compte le numéro de facture
def actes_gen(nbMax):
    
    def pdf_gen(nbMax):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt = "Fichier PDF de TEST !",
            ln = 1, align = 'C')
        pdf.cell(200, 10, txt = "Utilisable pour le PJDispatch.",
            ln = 2, align = 'C')

        pdfMin = 1

        while pdfMin < nbMax : 
            pdf.output(f"PDF_{str(pdfMin).zfill(9)}.pdf")
            pdfMin = pdfMin + 1

 #--------------------------------------------------------------------------------------------------------------------

    nbMin = 1
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
                    (random.choice(list(prestation_dict.values())))     +   #Dictionnaire des prestations
                    (random.choice(list(compteur_dict.values())))           #Dictionnaire du compteur (celui-ci n'est pas dans un fichier à part) (Ligne .44)
                    )
            
            f.close() #Ferme le fichier à la fin de l'écriture
            
            nbMin += 1 #Incrémentation de 1 de nbMin afin d'éviter la boucle infinie
            pdf_gen(nbMax)

actes_gen(50)   #Modifier le chiffre par le nombre factures que vous voulez générer.


