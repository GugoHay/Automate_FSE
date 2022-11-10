# PACKAGE CREATOR #
- Cette application est là pour aider à la creation de package, éditeur ou autres..

# CAS PARTICULIER #
- Dans le package un dossier "Certificats" doit être éxistant, si ce n'est pas le cas, vous ne pourrez pas ouvrir l'application


# UTILISATION #
METTRE L'EXECUTABLE DE L'EDITEUR DANS LE PACKAGE AVANT L'OUVERTURE DE L'APPLICATION


# VALEUR MIF #
A L'EXECUTION DE L'APPLICATION, IL FAUT PATIENTEZ QUELQUES INSTANT
- L'APPLICATION CREER UN FICHIER PARAM.PAR ([EXEC]CmdShow=H)
- L'APPLICATION OUVRE PYXVITAL EN MODE MASQUEE
- LANCE LA FONCTION OH (LIRE CONFIG EN MODE MASQUE)
- LIS LE FICHIER .MIF AFIN DE RECUPERER LA VALEUR DU NUMERO D'AGREMENT PROGICIEL
- AFFICHE CETTE VALEUR EN HAUT A DROITE (ENCADRER ROUGE)
-(Les fichiers .mif / start / stop / PARAM.par / Pyxvital_aaaammjj.log / sedtrace.txt) sont supprimé automatiquement du package à la fin de cette opperation.

- SI L'EXE N'EST PAS DANS LE PACKAGE, UN MESSAGE (Pyxvital.Exe manquant) EST INDIQUE


(Pour des raisons technique, les certificats scor inclus dans le dossier 'Certificats' seront déplacer vers un dossier nommée 'scor_der') (Vous n'avez pas à y toucher)

# SECTION TRANSFERT #
La catégorie de transfert vous permet de transferer des fichiers.
Les boutons parcourirs de gauche seront les chemins de vos fichier à déplacer
Les bouton parcourirs de droite, la destination
Appuyez sur "Transférer..." une fois sur de votre choix.


# SECTION DOSSIER #
A droite de l'appli vous retrouver 5 listes bleus, et 1 liste rouge.
Les listes vous ouvre le repertoire des editeurs ou socle technique choisis.


# SECTION PYXVITAL.ini #
Cocher simplement les cases dont vous souhaitez les sections dans le Pyxvital.ini

Attention : /!\
LA SECTION SCOR AJOUTE : 
- PJ=# dans la section [Repertoire] dans Pyxvital.ini
- Les lignes dans certificats.tab
- les certificats *.der dans le dossier Certificats
- la section [SCOR] dans le Pyxvital.ini

# SECTION SCRIPT #
Remplissez les champs :
- N° d'autorisation
- Nom editeur
- Version editeur

- Cliquez ensuite sur les boutons afins de générer le scripts de votre choix.

- SI VOUS AVEZ GENERER UN SCRIPT SANS LE VOULOIR, RECLIQUER SIMPLEMENT SUR LE BOUTON, CELA VA SUPPRIMER LES SCRIPTS CONCERNES


Cela change les "variable" suivantes dans les scripts directement :

- N° d'autorisation             <ctxlps:IDAM R="4">{EditeurNumName}</ctxlps:IDAM>
- Nom editeur                   <ctxlps:Nom>{EditeurName}</ctxlps:Nom>
- Version editeur               <ctxlps:Version>{EditeurVersion}</ctxlps:Version>


# AUTRE #
- Si vous rencontrez des bugs /
- Souhaitez de nouvelles fonctionnalitées / changements

Voir avec Gurguen Sahakian.