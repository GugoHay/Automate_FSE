# Cette première version de code, permet la generation de fichier .hif en prenant on compte le compteur à 8 chiffres.
# Le fichier est remplie par la variable 'txt'

# Ici aucune vérification n'est faite, et aucune données n'est transmise

txt = """[PRESTATION]
Quantite=
Coefficient=
Code_CCAM=
Code_compl_CCAM=
Modificateurs_CCAM=
Code_suppl_CCAM=
Code_affine=
Qualificatif_depense=
Domicile=
D_jf=
Nuit=
Urgence=
Code=
Montant_honoraires= 
"""

def filecreator():
    x,y = 1,15
    while x < y :
        with open("FSE" + str(x).zfill(8) + ".hif","w") as f:
            f.write(txt)
            f.close()
            x = x + 1


filecreator()
