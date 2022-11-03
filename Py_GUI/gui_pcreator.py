import tkinter
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageTk
import os
import shutil
import glob
import atexit
from numpy import column_stack

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("920x720")
app.title("Package Creator")
app.iconbitmap("assets/image_12.ico")



#VARIABLES LIST FOR MENU OPTION#
win_editeur_list = []
win_list = os.listdir(r"T:/Agrement Pyxistem/WIN")
for folder in win_list :
    win_editeur_list.append(folder)

osx_editeur_list = []
osx_list = os.listdir(r"T:/Agrement Pyxistem/OSX")
for folder in osx_list :
    osx_editeur_list.append(folder)

multi_editeur_list = []
multi_list = os.listdir(r"T:/Agrement Pyxistem/MULTI-OS")
for folder in multi_list :
    multi_editeur_list.append(folder)

linux_editeur_list = []
linux_list = os.listdir(r"T:/Agrement Pyxistem/LINUX")
for folder in linux_list :
    linux_editeur_list.append(folder)

ios_editeur_list = []
ios_list = os.listdir(r"T:/Agrement Pyxistem/IOS")
for folder in ios_list :
    ios_editeur_list.append(folder)

socle_technique_list = []
socle_list = os.listdir(r"T:/RESSOURCES SV/")
for folder in socle_list :
    socle_technique_list.append(folder)

win = r'T:/Agrement Pyxistem/WIN/'
multi = r"T:/Agrement Pyxistem/MULTI-OS/"
osx = r"T:/Agrement Pyxistem/OSX/"
linux = r"T:/Agrement Pyxistem/LINUX/"
ios = r"T:/Agrement Pyxistem/IOS/"
socleT = r"T:/RESSOURCES SV/"

pyx_ini = f"""
[Paramètres]
Log=PyxVital.log
CCAM_bis=O
Cabinet_groupe=O
NivDiagSTS=3
MAJ_Host=www.pyxistem.com
MAJ_SSL=O
Enregistre_Patients=N
VersionPraticien.par=1
VersionPatient.par=1
Verif_Patient=O
Date1_TPG=01/01/17
Date2_TPG=30/11/40
Verif_Forumes_STS=N

[Fichiers]
Message=PYXVITAL175
Compression=N

[SESAM-Vitale]
NomRessourcePS=
NomRessourceLecteur=
;NomRessourceNFC=
Numéro_FSE_fin=999999
NBMAX_FSE_LOT=50

[TPE]
Modes=N

[ADRi]
Automatique=N
Toujours_appeler=N

[SELAMC]
Ignore=O
Automatique=N
Host=ws.annuaireamc.fr

[Répertoires]
Fse=#
Lots=#
Fichiers=#
Arl=#
PJ=#
"""
certif_scor = f"""Certificats: table des certificats
Version 3.0
Adresse,Nom fichier certificat
01.011@01.scor.rss.fr,01.011@01.scor.rss.fr.der
01.021@01.scor.rss.fr,01.021@01.scor.rss.fr.der
01.022@01.scor.rss.fr,01.022@01.scor.rss.fr.der
01.031@01.scor.rss.fr,01.031@01.scor.rss.fr.der
01.041@01.scor.rss.fr,01.041@01.scor.rss.fr.der
01.051@01.scor.rss.fr,01.051@01.scor.rss.fr.der
01.061@01.scor.rss.fr,01.061@01.scor.rss.fr.der
01.071@01.scor.rss.fr,01.071@01.scor.rss.fr.der
01.072@01.scor.rss.fr,01.072@01.scor.rss.fr.der
01.081@01.scor.rss.fr,01.081@01.scor.rss.fr.der
01.091@01.scor.rss.fr,01.091@01.scor.rss.fr.der
01.101@01.scor.rss.fr,01.101@01.scor.rss.fr.der
01.111@01.scor.rss.fr,01.111@01.scor.rss.fr.der
01.121@01.scor.rss.fr,01.121@01.scor.rss.fr.der
01.131@01.scor.rss.fr,01.131@01.scor.rss.fr.der
01.141@01.scor.rss.fr,01.141@01.scor.rss.fr.der
01.151@01.scor.rss.fr,01.151@01.scor.rss.fr.der
01.161@01.scor.rss.fr,01.161@01.scor.rss.fr.der
01.171@01.scor.rss.fr,01.171@01.scor.rss.fr.der
01.181@01.scor.rss.fr,01.181@01.scor.rss.fr.der
01.191@01.scor.rss.fr,01.191@01.scor.rss.fr.der
01.201@01.scor.rss.fr,01.201@01.scor.rss.fr.der
01.202@01.scor.rss.fr,01.202@01.scor.rss.fr.der
01.211@01.scor.rss.fr,01.211@01.scor.rss.fr.der
01.221@01.scor.rss.fr,01.221@01.scor.rss.fr.der
01.231@01.scor.rss.fr,01.231@01.scor.rss.fr.der
01.241@01.scor.rss.fr,01.241@01.scor.rss.fr.der
01.251@01.scor.rss.fr,01.251@01.scor.rss.fr.der
01.252@01.scor.rss.fr,01.252@01.scor.rss.fr.der
01.261@01.scor.rss.fr,01.261@01.scor.rss.fr.der
01.271@01.scor.rss.fr,01.271@01.scor.rss.fr.der
01.281@01.scor.rss.fr,01.281@01.scor.rss.fr.der
01.291@01.scor.rss.fr,01.291@01.scor.rss.fr.der
01.292@01.scor.rss.fr,01.292@01.scor.rss.fr.der
01.301@01.scor.rss.fr,01.301@01.scor.rss.fr.der
01.311@01.scor.rss.fr,01.311@01.scor.rss.fr.der
01.321@01.scor.rss.fr,01.321@01.scor.rss.fr.der
01.331@01.scor.rss.fr,01.331@01.scor.rss.fr.der
01.341@01.scor.rss.fr,01.341@01.scor.rss.fr.der
01.342@01.scor.rss.fr,01.342@01.scor.rss.fr.der
01.351@01.scor.rss.fr,01.351@01.scor.rss.fr.der
01.361@01.scor.rss.fr,01.361@01.scor.rss.fr.der
01.371@01.scor.rss.fr,01.371@01.scor.rss.fr.der
01.381@01.scor.rss.fr,01.381@01.scor.rss.fr.der
01.382@01.scor.rss.fr,01.382@01.scor.rss.fr.der
01.391@01.scor.rss.fr,01.391@01.scor.rss.fr.der
01.401@01.scor.rss.fr,01.401@01.scor.rss.fr.der
01.411@01.scor.rss.fr,01.411@01.scor.rss.fr.der
01.421@01.scor.rss.fr,01.421@01.scor.rss.fr.der
01.422@01.scor.rss.fr,01.422@01.scor.rss.fr.der
01.431@01.scor.rss.fr,01.431@01.scor.rss.fr.der
01.441@01.scor.rss.fr,01.441@01.scor.rss.fr.der
01.442@01.scor.rss.fr,01.442@01.scor.rss.fr.der
01.451@01.scor.rss.fr,01.451@01.scor.rss.fr.der
01.461@01.scor.rss.fr,01.461@01.scor.rss.fr.der
01.471@01.scor.rss.fr,01.471@01.scor.rss.fr.der
01.481@01.scor.rss.fr,01.481@01.scor.rss.fr.der
01.491@01.scor.rss.fr,01.491@01.scor.rss.fr.der
01.492@01.scor.rss.fr,01.492@01.scor.rss.fr.der
01.501@01.scor.rss.fr,01.501@01.scor.rss.fr.der
01.511@01.scor.rss.fr,01.511@01.scor.rss.fr.der
01.521@01.scor.rss.fr,01.521@01.scor.rss.fr.der
01.531@01.scor.rss.fr,01.531@01.scor.rss.fr.der
01.541@01.scor.rss.fr,01.541@01.scor.rss.fr.der
01.542@01.scor.rss.fr,01.542@01.scor.rss.fr.der
01.551@01.scor.rss.fr,01.551@01.scor.rss.fr.der
01.561@01.scor.rss.fr,01.561@01.scor.rss.fr.der
01.571@01.scor.rss.fr,01.571@01.scor.rss.fr.der
01.572@01.scor.rss.fr,01.572@01.scor.rss.fr.der
01.573@01.scor.rss.fr,01.573@01.scor.rss.fr.der
01.581@01.scor.rss.fr,01.581@01.scor.rss.fr.der
01.591@01.scor.rss.fr,01.591@01.scor.rss.fr.der
01.592@01.scor.rss.fr,01.592@01.scor.rss.fr.der
01.593@01.scor.rss.fr,01.593@01.scor.rss.fr.der
01.594@01.scor.rss.fr,01.594@01.scor.rss.fr.der
01.595@01.scor.rss.fr,01.595@01.scor.rss.fr.der
01.596@01.scor.rss.fr,01.596@01.scor.rss.fr.der
01.597@01.scor.rss.fr,01.597@01.scor.rss.fr.der
01.598@01.scor.rss.fr,01.598@01.scor.rss.fr.der
01.599@01.scor.rss.fr,01.599@01.scor.rss.fr.der
01.601@01.scor.rss.fr,01.601@01.scor.rss.fr.der
01.602@01.scor.rss.fr,01.602@01.scor.rss.fr.der
01.611@01.scor.rss.fr,01.611@01.scor.rss.fr.der
01.621@01.scor.rss.fr,01.621@01.scor.rss.fr.der
01.622@01.scor.rss.fr,01.622@01.scor.rss.fr.der
01.623@01.scor.rss.fr,01.623@01.scor.rss.fr.der
01.624@01.scor.rss.fr,01.624@01.scor.rss.fr.der
01.631@01.scor.rss.fr,01.631@01.scor.rss.fr.der
01.641@01.scor.rss.fr,01.641@01.scor.rss.fr.der
01.642@01.scor.rss.fr,01.642@01.scor.rss.fr.der
01.651@01.scor.rss.fr,01.651@01.scor.rss.fr.der
01.661@01.scor.rss.fr,01.661@01.scor.rss.fr.der
01.671@01.scor.rss.fr,01.671@01.scor.rss.fr.der
01.672@01.scor.rss.fr,01.672@01.scor.rss.fr.der
01.673@01.scor.rss.fr,01.673@01.scor.rss.fr.der
01.681@01.scor.rss.fr,01.681@01.scor.rss.fr.der
01.682@01.scor.rss.fr,01.682@01.scor.rss.fr.der
01.691@01.scor.rss.fr,01.691@01.scor.rss.fr.der
01.692@01.scor.rss.fr,01.692@01.scor.rss.fr.der
01.701@01.scor.rss.fr,01.701@01.scor.rss.fr.der
01.711@01.scor.rss.fr,01.711@01.scor.rss.fr.der
01.721@01.scor.rss.fr,01.721@01.scor.rss.fr.der
01.731@01.scor.rss.fr,01.731@01.scor.rss.fr.der
01.741@01.scor.rss.fr,01.741@01.scor.rss.fr.der
01.751@01.scor.rss.fr,01.751@01.scor.rss.fr.der
01.761@01.scor.rss.fr,01.761@01.scor.rss.fr.der
01.762@01.scor.rss.fr,01.762@01.scor.rss.fr.der
01.763@01.scor.rss.fr,01.763@01.scor.rss.fr.der
01.764@01.scor.rss.fr,01.764@01.scor.rss.fr.der
01.771@01.scor.rss.fr,01.771@01.scor.rss.fr.der
01.781@01.scor.rss.fr,01.781@01.scor.rss.fr.der
01.791@01.scor.rss.fr,01.791@01.scor.rss.fr.der
01.801@01.scor.rss.fr,01.801@01.scor.rss.fr.der
01.811@01.scor.rss.fr,01.811@01.scor.rss.fr.der
01.821@01.scor.rss.fr,01.821@01.scor.rss.fr.der
01.831@01.scor.rss.fr,01.831@01.scor.rss.fr.der
01.841@01.scor.rss.fr,01.841@01.scor.rss.fr.der
01.851@01.scor.rss.fr,01.851@01.scor.rss.fr.der
01.861@01.scor.rss.fr,01.861@01.scor.rss.fr.der
01.871@01.scor.rss.fr,01.871@01.scor.rss.fr.der
01.881@01.scor.rss.fr,01.881@01.scor.rss.fr.der
01.891@01.scor.rss.fr,01.891@01.scor.rss.fr.der
01.901@01.scor.rss.fr,01.901@01.scor.rss.fr.der
01.909@01.scor.rss.fr,01.909@01.scor.rss.fr.der
01.911@01.scor.rss.fr,01.911@01.scor.rss.fr.der
01.921@01.scor.rss.fr,01.921@01.scor.rss.fr.der
01.931@01.scor.rss.fr,01.931@01.scor.rss.fr.der
01.941@01.scor.rss.fr,01.941@01.scor.rss.fr.der
01.951@01.scor.rss.fr,01.951@01.scor.rss.fr.der
01.971@01.scor.rss.fr,01.971@01.scor.rss.fr.der
01.972@01.scor.rss.fr,01.972@01.scor.rss.fr.der
01.973@01.scor.rss.fr,01.973@01.scor.rss.fr.der
01.974@01.scor.rss.fr,01.974@01.scor.rss.fr.der
01.976@01.scor.rss.fr,01.976@01.scor.rss.fr.der
02.01@02.scor.rss.fr,02.01@02.scor.rss.fr.der
02.02@02.scor.rss.fr,02.02@02.scor.rss.fr.der
02.03@02.scor.rss.fr,02.03@02.scor.rss.fr.der
02.04@02.scor.rss.fr,02.04@02.scor.rss.fr.der
02.06@02.scor.rss.fr,02.06@02.scor.rss.fr.der
02.11@02.scor.rss.fr,02.11@02.scor.rss.fr.der
02.24@02.scor.rss.fr,02.24@02.scor.rss.fr.der
02.27@02.scor.rss.fr,02.27@02.scor.rss.fr.der
02.28@02.scor.rss.fr,02.28@02.scor.rss.fr.der
02.32@02.scor.rss.fr,02.32@02.scor.rss.fr.der
02.44@02.scor.rss.fr,02.44@02.scor.rss.fr.der
02.52@02.scor.rss.fr,02.52@02.scor.rss.fr.der
02.53@02.scor.rss.fr,02.53@02.scor.rss.fr.der
02.75@02.scor.rss.fr,02.75@02.scor.rss.fr.der
02.76@02.scor.rss.fr,02.76@02.scor.rss.fr.der
02.84@02.scor.rss.fr,02.84@02.scor.rss.fr.der
02.93@02.scor.rss.fr,02.93@02.scor.rss.fr.der
02.94@02.scor.rss.fr,02.94@02.scor.rss.fr.der
03.01@03.scor.rss.fr,03.01@03.scor.rss.fr.der
03.02@03.scor.rss.fr,03.02@03.scor.rss.fr.der
03.03@03.scor.rss.fr,03.03@03.scor.rss.fr.der
03.04@03.scor.rss.fr,03.04@03.scor.rss.fr.der
03.06@03.scor.rss.fr,03.06@03.scor.rss.fr.der
03.11@03.scor.rss.fr,03.11@03.scor.rss.fr.der
03.24@03.scor.rss.fr,03.24@03.scor.rss.fr.der
03.27@03.scor.rss.fr,03.27@03.scor.rss.fr.der
03.28@03.scor.rss.fr,03.28@03.scor.rss.fr.der
03.32@03.scor.rss.fr,03.32@03.scor.rss.fr.der
03.44@03.scor.rss.fr,03.44@03.scor.rss.fr.der
03.52@03.scor.rss.fr,03.52@03.scor.rss.fr.der
03.53@03.scor.rss.fr,03.53@03.scor.rss.fr.der
03.75@03.scor.rss.fr,03.75@03.scor.rss.fr.der
03.76@03.scor.rss.fr,03.76@03.scor.rss.fr.der
03.84@03.scor.rss.fr,03.84@03.scor.rss.fr.der
03.93@03.scor.rss.fr,03.93@03.scor.rss.fr.der
03.94@03.scor.rss.fr,03.94@03.scor.rss.fr.der
04.01@04.scor.rss.fr,04.01@04.scor.rss.fr.der
04.02@04.scor.rss.fr,04.02@04.scor.rss.fr.der
04.03@04.scor.rss.fr,04.03@04.scor.rss.fr.der
04.04@04.scor.rss.fr,04.04@04.scor.rss.fr.der
04.06@04.scor.rss.fr,04.06@04.scor.rss.fr.der
04.11@04.scor.rss.fr,04.11@04.scor.rss.fr.der
04.24@04.scor.rss.fr,04.24@04.scor.rss.fr.der
04.27@04.scor.rss.fr,04.27@04.scor.rss.fr.der
04.28@04.scor.rss.fr,04.28@04.scor.rss.fr.der
04.32@04.scor.rss.fr,04.32@04.scor.rss.fr.der
04.44@04.scor.rss.fr,04.44@04.scor.rss.fr.der
04.52@04.scor.rss.fr,04.52@04.scor.rss.fr.der
04.53@04.scor.rss.fr,04.53@04.scor.rss.fr.der
04.75@04.scor.rss.fr,04.75@04.scor.rss.fr.der
04.76@04.scor.rss.fr,04.76@04.scor.rss.fr.der
04.84@04.scor.rss.fr,04.84@04.scor.rss.fr.der
04.93@04.scor.rss.fr,04.93@04.scor.rss.fr.der
04.94@04.scor.rss.fr,04.94@04.scor.rss.fr.der
05.01@05.scor.rss.fr,05.01@05.scor.rss.fr.der
05.02@05.scor.rss.fr,05.02@05.scor.rss.fr.der
05.03@05.scor.rss.fr,05.03@05.scor.rss.fr.der
05.04@05.scor.rss.fr,05.04@05.scor.rss.fr.der
05.06@05.scor.rss.fr,05.06@05.scor.rss.fr.der
05.11@05.scor.rss.fr,05.11@05.scor.rss.fr.der
05.24@05.scor.rss.fr,05.24@05.scor.rss.fr.der
05.27@05.scor.rss.fr,05.27@05.scor.rss.fr.der
05.28@05.scor.rss.fr,05.28@05.scor.rss.fr.der
05.32@05.scor.rss.fr,05.32@05.scor.rss.fr.der
05.44@05.scor.rss.fr,05.44@05.scor.rss.fr.der
05.52@05.scor.rss.fr,05.52@05.scor.rss.fr.der
05.53@05.scor.rss.fr,05.53@05.scor.rss.fr.der
05.75@05.scor.rss.fr,05.75@05.scor.rss.fr.der
05.76@05.scor.rss.fr,05.76@05.scor.rss.fr.der
05.84@05.scor.rss.fr,05.84@05.scor.rss.fr.der
05.93@05.scor.rss.fr,05.93@05.scor.rss.fr.der
05.94@05.scor.rss.fr,05.94@05.scor.rss.fr.der
06.01@06.scor.rss.fr,06.01@06.scor.rss.fr.der
06.02@06.scor.rss.fr,06.02@06.scor.rss.fr.der
06.03@06.scor.rss.fr,06.03@06.scor.rss.fr.der
06.04@06.scor.rss.fr,06.04@06.scor.rss.fr.der
06.06@06.scor.rss.fr,06.06@06.scor.rss.fr.der
06.11@06.scor.rss.fr,06.11@06.scor.rss.fr.der
06.24@06.scor.rss.fr,06.24@06.scor.rss.fr.der
06.27@06.scor.rss.fr,06.27@06.scor.rss.fr.der
06.28@06.scor.rss.fr,06.28@06.scor.rss.fr.der
06.32@06.scor.rss.fr,06.32@06.scor.rss.fr.der
06.44@06.scor.rss.fr,06.44@06.scor.rss.fr.der
06.52@06.scor.rss.fr,06.52@06.scor.rss.fr.der
06.53@06.scor.rss.fr,06.53@06.scor.rss.fr.der
06.75@06.scor.rss.fr,06.75@06.scor.rss.fr.der
06.76@06.scor.rss.fr,06.76@06.scor.rss.fr.der
06.84@06.scor.rss.fr,06.84@06.scor.rss.fr.der
06.93@06.scor.rss.fr,06.93@06.scor.rss.fr.der
06.94@06.scor.rss.fr,06.94@06.scor.rss.fr.der
07.01@07.scor.rss.fr,07.01@07.scor.rss.fr.der
07.02@07.scor.rss.fr,07.02@07.scor.rss.fr.der
07.03@07.scor.rss.fr,07.03@07.scor.rss.fr.der
07.04@07.scor.rss.fr,07.04@07.scor.rss.fr.der
07.06@07.scor.rss.fr,07.06@07.scor.rss.fr.der
07.11@07.scor.rss.fr,07.11@07.scor.rss.fr.der
07.24@07.scor.rss.fr,07.24@07.scor.rss.fr.der
07.27@07.scor.rss.fr,07.27@07.scor.rss.fr.der
07.28@07.scor.rss.fr,07.28@07.scor.rss.fr.der
07.32@07.scor.rss.fr,07.32@07.scor.rss.fr.der
07.44@07.scor.rss.fr,07.44@07.scor.rss.fr.der
07.52@07.scor.rss.fr,07.52@07.scor.rss.fr.der
07.53@07.scor.rss.fr,07.53@07.scor.rss.fr.der
07.75@07.scor.rss.fr,07.75@07.scor.rss.fr.der
07.76@07.scor.rss.fr,07.76@07.scor.rss.fr.der
07.84@07.scor.rss.fr,07.84@07.scor.rss.fr.der
07.93@07.scor.rss.fr,07.93@07.scor.rss.fr.der
07.94@07.scor.rss.fr,07.94@07.scor.rss.fr.der
08.01@08.scor.rss.fr,08.01@08.scor.rss.fr.der
08.02@08.scor.rss.fr,08.02@08.scor.rss.fr.der
08.03@08.scor.rss.fr,08.03@08.scor.rss.fr.der
08.04@08.scor.rss.fr,08.04@08.scor.rss.fr.der
08.06@08.scor.rss.fr,08.06@08.scor.rss.fr.der
08.11@08.scor.rss.fr,08.11@08.scor.rss.fr.der
08.24@08.scor.rss.fr,08.24@08.scor.rss.fr.der
08.27@08.scor.rss.fr,08.27@08.scor.rss.fr.der
08.28@08.scor.rss.fr,08.28@08.scor.rss.fr.der
08.32@08.scor.rss.fr,08.32@08.scor.rss.fr.der
08.44@08.scor.rss.fr,08.44@08.scor.rss.fr.der
08.52@08.scor.rss.fr,08.52@08.scor.rss.fr.der
08.53@08.scor.rss.fr,08.53@08.scor.rss.fr.der
08.75@08.scor.rss.fr,08.75@08.scor.rss.fr.der
08.76@08.scor.rss.fr,08.76@08.scor.rss.fr.der
08.84@08.scor.rss.fr,08.84@08.scor.rss.fr.der
08.93@08.scor.rss.fr,08.93@08.scor.rss.fr.der
08.94@08.scor.rss.fr,08.94@08.scor.rss.fr.der
10.01@10.scor.rss.fr,10.01@10.scor.rss.fr.der
10.02@10.scor.rss.fr,10.02@10.scor.rss.fr.der
10.03@10.scor.rss.fr,10.03@10.scor.rss.fr.der
10.04@10.scor.rss.fr,10.04@10.scor.rss.fr.der
10.06@10.scor.rss.fr,10.06@10.scor.rss.fr.der
10.11@10.scor.rss.fr,10.11@10.scor.rss.fr.der
10.24@10.scor.rss.fr,10.24@10.scor.rss.fr.der
10.27@10.scor.rss.fr,10.27@10.scor.rss.fr.der
10.28@10.scor.rss.fr,10.28@10.scor.rss.fr.der
10.32@10.scor.rss.fr,10.32@10.scor.rss.fr.der
10.44@10.scor.rss.fr,10.44@10.scor.rss.fr.der
10.52@10.scor.rss.fr,10.52@10.scor.rss.fr.der
10.53@10.scor.rss.fr,10.53@10.scor.rss.fr.der
10.75@10.scor.rss.fr,10.75@10.scor.rss.fr.der
10.76@10.scor.rss.fr,10.76@10.scor.rss.fr.der
10.84@10.scor.rss.fr,10.84@10.scor.rss.fr.der
10.93@10.scor.rss.fr,10.93@10.scor.rss.fr.der
10.94@10.scor.rss.fr,10.94@10.scor.rss.fr.der
14.01@14.scor.rss.fr,14.01@14.scor.rss.fr.der
14.02@14.scor.rss.fr,14.02@14.scor.rss.fr.der
14.03@14.scor.rss.fr,14.03@14.scor.rss.fr.der
14.04@14.scor.rss.fr,14.04@14.scor.rss.fr.der
14.06@14.scor.rss.fr,14.06@14.scor.rss.fr.der
14.11@14.scor.rss.fr,14.11@14.scor.rss.fr.der
14.24@14.scor.rss.fr,14.24@14.scor.rss.fr.der
14.27@14.scor.rss.fr,14.27@14.scor.rss.fr.der
14.28@14.scor.rss.fr,14.28@14.scor.rss.fr.der
14.32@14.scor.rss.fr,14.32@14.scor.rss.fr.der
14.44@14.scor.rss.fr,14.44@14.scor.rss.fr.der
14.52@14.scor.rss.fr,14.52@14.scor.rss.fr.der
14.53@14.scor.rss.fr,14.53@14.scor.rss.fr.der
14.75@14.scor.rss.fr,14.75@14.scor.rss.fr.der
14.76@14.scor.rss.fr,14.76@14.scor.rss.fr.der
14.84@14.scor.rss.fr,14.84@14.scor.rss.fr.der
14.93@14.scor.rss.fr,14.93@14.scor.rss.fr.der
14.94@14.scor.rss.fr,14.94@14.scor.rss.fr.der
15.01@15.scor.rss.fr,15.01@15.scor.rss.fr.der
15.02@15.scor.rss.fr,15.02@15.scor.rss.fr.der
15.03@15.scor.rss.fr,15.03@15.scor.rss.fr.der
15.04@15.scor.rss.fr,15.04@15.scor.rss.fr.der
15.06@15.scor.rss.fr,15.06@15.scor.rss.fr.der
15.11@15.scor.rss.fr,15.11@15.scor.rss.fr.der
15.24@15.scor.rss.fr,15.24@15.scor.rss.fr.der
15.27@15.scor.rss.fr,15.27@15.scor.rss.fr.der
15.28@15.scor.rss.fr,15.28@15.scor.rss.fr.der
15.32@15.scor.rss.fr,15.32@15.scor.rss.fr.der
15.44@15.scor.rss.fr,15.44@15.scor.rss.fr.der
15.52@15.scor.rss.fr,15.52@15.scor.rss.fr.der
15.53@15.scor.rss.fr,15.53@15.scor.rss.fr.der
15.75@15.scor.rss.fr,15.75@15.scor.rss.fr.der
15.76@15.scor.rss.fr,15.76@15.scor.rss.fr.der
15.84@15.scor.rss.fr,15.84@15.scor.rss.fr.der
15.93@15.scor.rss.fr,15.93@15.scor.rss.fr.der
15.94@15.scor.rss.fr,15.94@15.scor.rss.fr.der
16.01@16.scor.rss.fr,16.01@16.scor.rss.fr.der
16.02@16.scor.rss.fr,16.02@16.scor.rss.fr.der
16.03@16.scor.rss.fr,16.03@16.scor.rss.fr.der
16.04@16.scor.rss.fr,16.04@16.scor.rss.fr.der
16.06@16.scor.rss.fr,16.06@16.scor.rss.fr.der
16.11@16.scor.rss.fr,16.11@16.scor.rss.fr.der
16.24@16.scor.rss.fr,16.24@16.scor.rss.fr.der
16.27@16.scor.rss.fr,16.27@16.scor.rss.fr.der
16.28@16.scor.rss.fr,16.28@16.scor.rss.fr.der
16.32@16.scor.rss.fr,16.32@16.scor.rss.fr.der
16.44@16.scor.rss.fr,16.44@16.scor.rss.fr.der
16.52@16.scor.rss.fr,16.52@16.scor.rss.fr.der
16.53@16.scor.rss.fr,16.53@16.scor.rss.fr.der
16.75@16.scor.rss.fr,16.75@16.scor.rss.fr.der
16.76@16.scor.rss.fr,16.76@16.scor.rss.fr.der
16.84@16.scor.rss.fr,16.84@16.scor.rss.fr.der
16.93@16.scor.rss.fr,16.93@16.scor.rss.fr.der
16.94@16.scor.rss.fr,16.94@16.scor.rss.fr.der
17.01@17.scor.rss.fr,17.01@17.scor.rss.fr.der
17.02@17.scor.rss.fr,17.02@17.scor.rss.fr.der
17.03@17.scor.rss.fr,17.03@17.scor.rss.fr.der
17.04@17.scor.rss.fr,17.04@17.scor.rss.fr.der
17.06@17.scor.rss.fr,17.06@17.scor.rss.fr.der
17.11@17.scor.rss.fr,17.11@17.scor.rss.fr.der
17.24@17.scor.rss.fr,17.24@17.scor.rss.fr.der
17.27@17.scor.rss.fr,17.27@17.scor.rss.fr.der
17.28@17.scor.rss.fr,17.28@17.scor.rss.fr.der
17.32@17.scor.rss.fr,17.32@17.scor.rss.fr.der
17.44@17.scor.rss.fr,17.44@17.scor.rss.fr.der
17.52@17.scor.rss.fr,17.52@17.scor.rss.fr.der
17.53@17.scor.rss.fr,17.53@17.scor.rss.fr.der
17.75@17.scor.rss.fr,17.75@17.scor.rss.fr.der
17.76@17.scor.rss.fr,17.76@17.scor.rss.fr.der
17.84@17.scor.rss.fr,17.84@17.scor.rss.fr.der
17.93@17.scor.rss.fr,17.93@17.scor.rss.fr.der
17.94@17.scor.rss.fr,17.94@17.scor.rss.fr.der
90.01@90.scor.rss.fr,90.01@90.scor.rss.fr.der
90.02@90.scor.rss.fr,90.02@90.scor.rss.fr.der
90.03@90.scor.rss.fr,90.03@90.scor.rss.fr.der
90.04@90.scor.rss.fr,90.04@90.scor.rss.fr.der
90.06@90.scor.rss.fr,90.06@90.scor.rss.fr.der
90.11@90.scor.rss.fr,90.11@90.scor.rss.fr.der
90.24@90.scor.rss.fr,90.24@90.scor.rss.fr.der
90.27@90.scor.rss.fr,90.27@90.scor.rss.fr.der
90.28@90.scor.rss.fr,90.28@90.scor.rss.fr.der
90.32@90.scor.rss.fr,90.32@90.scor.rss.fr.der
90.44@90.scor.rss.fr,90.44@90.scor.rss.fr.der
90.52@90.scor.rss.fr,90.52@90.scor.rss.fr.der
90.53@90.scor.rss.fr,90.53@90.scor.rss.fr.der
90.75@90.scor.rss.fr,90.75@90.scor.rss.fr.der
90.76@90.scor.rss.fr,90.76@90.scor.rss.fr.der
90.84@90.scor.rss.fr,90.84@90.scor.rss.fr.der
90.93@90.scor.rss.fr,90.93@90.scor.rss.fr.der
90.94@90.scor.rss.fr,90.94@90.scor.rss.fr.der
91.01@91.scor.rss.fr,91.01@91.scor.rss.fr.der
91.02@91.scor.rss.fr,91.02@91.scor.rss.fr.der
91.03@91.scor.rss.fr,91.03@91.scor.rss.fr.der
91.04@91.scor.rss.fr,91.04@91.scor.rss.fr.der
91.06@91.scor.rss.fr,91.06@91.scor.rss.fr.der
91.11@91.scor.rss.fr,91.11@91.scor.rss.fr.der
91.24@91.scor.rss.fr,91.24@91.scor.rss.fr.der
91.27@91.scor.rss.fr,91.27@91.scor.rss.fr.der
91.28@91.scor.rss.fr,91.28@91.scor.rss.fr.der
91.32@91.scor.rss.fr,91.32@91.scor.rss.fr.der
91.44@91.scor.rss.fr,91.44@91.scor.rss.fr.der
91.52@91.scor.rss.fr,91.52@91.scor.rss.fr.der
91.53@91.scor.rss.fr,91.53@91.scor.rss.fr.der
91.75@91.scor.rss.fr,91.75@91.scor.rss.fr.der
91.76@91.scor.rss.fr,91.76@91.scor.rss.fr.der
91.84@91.scor.rss.fr,91.84@91.scor.rss.fr.der
91.93@91.scor.rss.fr,91.93@91.scor.rss.fr.der
91.94@91.scor.rss.fr,91.94@91.scor.rss.fr.der
92.01@92.scor.rss.fr,92.01@92.scor.rss.fr.der
92.02@92.scor.rss.fr,92.02@92.scor.rss.fr.der
92.03@92.scor.rss.fr,92.03@92.scor.rss.fr.der
92.04@92.scor.rss.fr,92.04@92.scor.rss.fr.der
92.06@92.scor.rss.fr,92.06@92.scor.rss.fr.der
92.11@92.scor.rss.fr,92.11@92.scor.rss.fr.der
92.24@92.scor.rss.fr,92.24@92.scor.rss.fr.der
92.27@92.scor.rss.fr,92.27@92.scor.rss.fr.der
92.28@92.scor.rss.fr,92.28@92.scor.rss.fr.der
92.32@92.scor.rss.fr,92.32@92.scor.rss.fr.der
92.44@92.scor.rss.fr,92.44@92.scor.rss.fr.der
92.52@92.scor.rss.fr,92.52@92.scor.rss.fr.der
92.53@92.scor.rss.fr,92.53@92.scor.rss.fr.der
92.75@92.scor.rss.fr,92.75@92.scor.rss.fr.der
92.76@92.scor.rss.fr,92.76@92.scor.rss.fr.der
92.84@92.scor.rss.fr,92.84@92.scor.rss.fr.der
92.93@92.scor.rss.fr,92.93@92.scor.rss.fr.der
92.94@92.scor.rss.fr,92.94@92.scor.rss.fr.der
93.01@93.scor.rss.fr,93.01@93.scor.rss.fr.der
93.02@93.scor.rss.fr,93.02@93.scor.rss.fr.der
93.03@93.scor.rss.fr,93.03@93.scor.rss.fr.der
93.04@93.scor.rss.fr,93.04@93.scor.rss.fr.der
93.06@93.scor.rss.fr,93.06@93.scor.rss.fr.der
93.11@93.scor.rss.fr,93.11@93.scor.rss.fr.der
93.24@93.scor.rss.fr,93.24@93.scor.rss.fr.der
93.27@93.scor.rss.fr,93.27@93.scor.rss.fr.der
93.28@93.scor.rss.fr,93.28@93.scor.rss.fr.der
93.32@93.scor.rss.fr,93.32@93.scor.rss.fr.der
93.44@93.scor.rss.fr,93.44@93.scor.rss.fr.der
93.52@93.scor.rss.fr,93.52@93.scor.rss.fr.der
93.53@93.scor.rss.fr,93.53@93.scor.rss.fr.der
93.75@93.scor.rss.fr,93.75@93.scor.rss.fr.der
93.76@93.scor.rss.fr,93.76@93.scor.rss.fr.der
93.84@93.scor.rss.fr,93.84@93.scor.rss.fr.der
93.93@93.scor.rss.fr,93.93@93.scor.rss.fr.der
93.94@93.scor.rss.fr,93.94@93.scor.rss.fr.der
94.01@94.scor.rss.fr,94.01@94.scor.rss.fr.der
94.02@94.scor.rss.fr,94.02@94.scor.rss.fr.der
94.03@94.scor.rss.fr,94.03@94.scor.rss.fr.der
94.04@94.scor.rss.fr,94.04@94.scor.rss.fr.der
94.06@94.scor.rss.fr,94.06@94.scor.rss.fr.der
94.11@94.scor.rss.fr,94.11@94.scor.rss.fr.der
94.24@94.scor.rss.fr,94.24@94.scor.rss.fr.der
94.27@94.scor.rss.fr,94.27@94.scor.rss.fr.der
94.28@94.scor.rss.fr,94.28@94.scor.rss.fr.der
94.32@94.scor.rss.fr,94.32@94.scor.rss.fr.der
94.44@94.scor.rss.fr,94.44@94.scor.rss.fr.der
94.52@94.scor.rss.fr,94.52@94.scor.rss.fr.der
94.53@94.scor.rss.fr,94.53@94.scor.rss.fr.der
94.75@94.scor.rss.fr,94.75@94.scor.rss.fr.der
94.76@94.scor.rss.fr,94.76@94.scor.rss.fr.der
94.84@94.scor.rss.fr,94.84@94.scor.rss.fr.der
94.93@94.scor.rss.fr,94.93@94.scor.rss.fr.der
94.94@94.scor.rss.fr,94.94@94.scor.rss.fr.der
95.01@95.scor.rss.fr,95.01@95.scor.rss.fr.der
95.02@95.scor.rss.fr,95.02@95.scor.rss.fr.der
95.03@95.scor.rss.fr,95.03@95.scor.rss.fr.der
95.04@95.scor.rss.fr,95.04@95.scor.rss.fr.der
95.06@95.scor.rss.fr,95.06@95.scor.rss.fr.der
95.11@95.scor.rss.fr,95.11@95.scor.rss.fr.der
95.24@95.scor.rss.fr,95.24@95.scor.rss.fr.der
95.27@95.scor.rss.fr,95.27@95.scor.rss.fr.der
95.28@95.scor.rss.fr,95.28@95.scor.rss.fr.der
95.32@95.scor.rss.fr,95.32@95.scor.rss.fr.der
95.44@95.scor.rss.fr,95.44@95.scor.rss.fr.der
95.52@95.scor.rss.fr,95.52@95.scor.rss.fr.der
95.53@95.scor.rss.fr,95.53@95.scor.rss.fr.der
95.75@95.scor.rss.fr,95.75@95.scor.rss.fr.der
95.76@95.scor.rss.fr,95.76@95.scor.rss.fr.der
95.84@95.scor.rss.fr,95.84@95.scor.rss.fr.der
95.93@95.scor.rss.fr,95.93@95.scor.rss.fr.der
95.94@95.scor.rss.fr,95.94@95.scor.rss.fr.der
96.01@96.scor.rss.fr,96.01@96.scor.rss.fr.der
96.02@96.scor.rss.fr,96.02@96.scor.rss.fr.der
96.03@96.scor.rss.fr,96.03@96.scor.rss.fr.der
96.04@96.scor.rss.fr,96.04@96.scor.rss.fr.der
96.06@96.scor.rss.fr,96.06@96.scor.rss.fr.der
96.11@96.scor.rss.fr,96.11@96.scor.rss.fr.der
96.24@96.scor.rss.fr,96.24@96.scor.rss.fr.der
96.27@96.scor.rss.fr,96.27@96.scor.rss.fr.der
96.28@96.scor.rss.fr,96.28@96.scor.rss.fr.der
96.32@96.scor.rss.fr,96.32@96.scor.rss.fr.der
96.44@96.scor.rss.fr,96.44@96.scor.rss.fr.der
96.52@96.scor.rss.fr,96.52@96.scor.rss.fr.der
96.53@96.scor.rss.fr,96.53@96.scor.rss.fr.der
96.75@96.scor.rss.fr,96.75@96.scor.rss.fr.der
96.76@96.scor.rss.fr,96.76@96.scor.rss.fr.der
96.84@96.scor.rss.fr,96.84@96.scor.rss.fr.der
96.93@96.scor.rss.fr,96.93@96.scor.rss.fr.der
96.94@96.scor.rss.fr,96.94@96.scor.rss.fr.der
99.01@99.scor.rss.fr,99.01@99.scor.rss.fr.der
99.02@99.scor.rss.fr,99.02@99.scor.rss.fr.der
99.03@99.scor.rss.fr,99.03@99.scor.rss.fr.der
99.04@99.scor.rss.fr,99.04@99.scor.rss.fr.der
99.06@99.scor.rss.fr,99.06@99.scor.rss.fr.der
99.11@99.scor.rss.fr,99.11@99.scor.rss.fr.der
99.24@99.scor.rss.fr,99.24@99.scor.rss.fr.der
99.27@99.scor.rss.fr,99.27@99.scor.rss.fr.der
99.28@99.scor.rss.fr,99.28@99.scor.rss.fr.der
99.32@99.scor.rss.fr,99.32@99.scor.rss.fr.der
99.44@99.scor.rss.fr,99.44@99.scor.rss.fr.der
99.52@99.scor.rss.fr,99.52@99.scor.rss.fr.der
99.53@99.scor.rss.fr,99.53@99.scor.rss.fr.der
99.75@99.scor.rss.fr,99.75@99.scor.rss.fr.der
99.76@99.scor.rss.fr,99.76@99.scor.rss.fr.der
99.84@99.scor.rss.fr,99.84@99.scor.rss.fr.der
99.93@99.scor.rss.fr,99.93@99.scor.rss.fr.der
99.94@99.scor.rss.fr,99.94@99.scor.rss.fr.der
amo,amo.der
amc,amc.der

"""
certif_ss_scor = f"""Certificats: table des certificats
Version 3.0
Adresse,Nom fichier certificat
amo,amo.der
amc,amc.der

"""
scor = f"""
[SCOR]
TailleMaxPJ=250
Adapte_version_PDF=O
Automatique=O
teste_version_PDF=N
"""
aldi = f"""
[ALDi]
URL=/lps
Automatique=N
"""
imti = f"""
[IMTi]
URL=/lps
"""
hri = f"""
[HRi]
URL=/lps
"""
dmti = f"""
[DMTi]
URL=/lps
"""
insi = f"""
[INSi]
Host=services-ps.ameli.fr
URL=/lps
Automatique=N
"""
apcv = f"""
[ECV]
Host=ias.apcv.sesam-vitale.fr
URL=/wssoap/apcv/auth/1/0
Envelope=apCV1env.txt
Body=apCV1body.txt

[ECV2]
Host=ias.apcv.sesam-vitale.fr
URL=/wssoap/apcv/auth/1/0
Envelope=apCV2env.txt
Body=apCV2body.txt

[ECV3]
Host=ias.apcv.sesam-vitale.fr
URL=/wssoap/apcv/auth/1/0
Envelope=apCV3env.txt
Body=apCV3body.txt

[ECV4]
Host=ias.apcv.sesam-vitale.fr
URL=/wssoap/apcv/sign/1/0
Envelope=apCV4env.txt
Body=apCV4body.txt
"""
srt = f"""
[SRT]
Outrepasse=CC8
"""


#FUNCTIONS#

def optionmenu_callback(choice):
    if choice in win_editeur_list:
        os.startfile(win + choice)
    elif choice in multi_editeur_list:
        os.startfile(multi + choice)
    elif choice in osx_editeur_list:
        os.startfile(osx + choice)
    elif choice in linux_editeur_list:
        os.startfile(linux + choice)
    elif choice in ios_editeur_list:
        os.startfile(ios + choice)
    elif choice in socle_technique_list:
        os.startfile(socleT + choice)

def button_event_adr():
    EditeurNumName = entry_ENN.get()
    EditeurVersion = entry_EV.get()
    EditeurName = entry_EN.get()
    with open("Scripts/ADRenv.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:urn="urn:ir:se_req_adr" xmlns:urn1="urn:siram:beneficiaire">
<soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
<wsse:Security>
%#include/AssertionCPS2
%#ifdef%/Vitale%#include/AssertionCV%#endif
</wsse:Security>
<ctxbam:ContexteBAM Version="01_02" xsi:schemaLocation="urn:siram:bam:ctxbam ../xsd/ctx/ROOT_ctxbam_CTXBAM_V01_02.xsd " Nature="CTXBAM" xmlns:ctxbam="urn:siram:bam:ctxbam" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<ctxbam:Id>%/Assertion_ID</ctxbam:Id>
<ctxbam:Temps>%/Connect/CPS/UTC</ctxbam:Temps>
<ctxbam:Emetteur>%/Praticien/PS/ADELI</ctxbam:Emetteur>
<ctxbam:COUVERTURE>
<ctxbam:GrandRegime>%/Patient/Médico_administratif/Code_régime</ctxbam:GrandRegime>
%#ifdef%/Patient/Médico_administratif/Caisse_gestionnaire<ctxbam:Organisme>%/Patient/Médico_administratif/Caisse_gestionnaire</ctxbam:Organisme>%#endif
%#ifdef%/Patient/Médico_administratif/Centre_gestionnaire<ctxbam:CodeCentre>%/Patient/Médico_administratif/Centre_gestionnaire</ctxbam:CodeCentre>%#endif
<ctxbam:ASSURE>
<ctxbam:Id>
<ctxbam:Num>%/Patient/Assuré/Numéro</ctxbam:Num>
<ctxbam:Cle>%/Patient/Assuré/Clé</ctxbam:Cle>
</ctxbam:Id>
</ctxbam:ASSURE>
<ctxbam:BENEFICIAIRE>
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel
<ctxbam:Nir>
<ctxbam:Num>%/Patient/Bénéficiaire/Numéro_individuel</ctxbam:Num>
<ctxbam:Cle>%/Patient/Bénéficiaire/Clé_individuel</ctxbam:Cle>
%#endif
%#ifdef%/Patient/Bénéficiaire/Date_individuel<ctxbam:DateCertification>%/Patient/Bénéficiaire/Date_individuel</ctxbam:DateCertification>%#endif
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel</ctxbam:Nir>%#endif
<ctxbam:DateNai>%/Patient/Bénéficiaire/Date_de_naissance</ctxbam:DateNai>
<ctxbam:Rang>%/Patient/Bénéficiaire/Rang_gémellaire</ctxbam:Rang>
</ctxbam:BENEFICIAIRE>
</ctxbam:COUVERTURE>
</ctxbam:ContexteBAM>
<ctxlps:ContexteLPS Nature="CTXLPS" Version="01_00" xsi:schemaLocation="urn:siram:lps:ctxlps xsd/CTX/ROOT_ctxlps_CTXLPS_V01_00.xsd" xmlns:ctxlps="urn:siram:lps:ctxlps" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<ctxlps:Id>%/Assertion_ID</ctxlps:Id>
<ctxlps:Temps>%/Connect/CPS/UTC</ctxlps:Temps>
<ctxlps:Emetteur>%/Praticien/PS/ADELI</ctxlps:Emetteur>
<ctxlps:LPS>
<ctxlps:IDAM R="4">{EditeurNumName}</ctxlps:IDAM>
<ctxlps:Version>{EditeurVersion}</ctxlps:Version>
<ctxlps:Instance>%/OID.%/Praticien/PS/ADELI</ctxlps:Instance>
<ctxlps:Nom>{EditeurName}</ctxlps:Nom>
</ctxlps:LPS>
</ctxlps:ContexteLPS>
<wsa:MessageID>%/MessageID</wsa:MessageID>
<wsa:Action>urn:adr:1.1.0:acquerirLesDroits</wsa:Action>
</soap:Header>
<soap:Body>
%#body
</soap:Body>
</soap:Envelope>
        """
        )
        f.close()
    with open("Scripts/ADRbody.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<urn:Requete>
<urn:DatedeReference>%/DateRef</urn:DatedeReference>
<urn:BeneficiaireDeSoins>
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel
<urn:NIRcertifie>
<urn:Num>%/Patient/Bénéficiaire/Numéro_individuel</urn:Num>
<urn:Cle>%/Patient/Bénéficiaire/Clé_individuel</urn:Cle>
</urn:NIRcertifie>
%#endif
<urn:DatedeNaissance>%/Patient/Bénéficiaire/Date_de_naissance</urn:DatedeNaissance>
<urn:SituationAdministrativeAMO>
<urn:RangdeNaissance>%/Patient/Bénéficiaire/Rang_gémellaire</urn:RangdeNaissance>
</urn:SituationAdministrativeAMO>
<urn:Assure>
<urn:NIRassure>
<urn:Num>%/Patient/Assuré/Numéro</urn:Num>
<urn:Cle>%/Patient/Assuré/Clé</urn:Cle>
</urn:NIRassure>
</urn:Assure>
</urn:BeneficiaireDeSoins>
</urn:Requete>
        """
        )
        f.close()
        #Fonction permettant de switch les checkbox
        done_adr.configure(state=tkinter.NORMAL)
        done_adr.toggle()
        done_adr.configure(state=tkinter.DISABLED)
def button_event_ald():
    EditeurNumName = entry_ENN.get()
    EditeurVersion = entry_EV.get()
    EditeurName = entry_EN.get()
    with open("Scripts/ALDenv.txt", "w" ,encoding="ANSI") as f:
        f.write(f"""
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:add="http://www.w3.org/2005/08/addressing" xmlns:urn="urn:siram:bam:ctxbam" xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:urn1="urn:oasis:names:tc:SAML:2.0:assertion" xmlns:xd="http://www.w3.org/2000/09/xmldsig#" xmlns:xe="http://www.w3.org/2001/04/xmlenc#" xmlns:urn2="urn:siram:lps:ctxlps" xmlns:aff="http://www.cnamts.fr/AffectionLongueDuree" xmlns:urn3="urn:rg:se_reqaldi" xmlns:urn4="urn:siram:partenairesante" xmlns:urn5="urn:siram:beneficiaire">
<soap:Header>
<add:MessageID>%/MessageID</add:MessageID>
<add:Action>urn:ald:1.0.0:lister</add:Action>
<oas:Security>
%#include/AssertionCPS
%#include/AssertionCV
</oas:Security>
<urn:ContexteBAM Version="01_02">
<urn:Id>%/Assertion_ID</urn:Id>
<urn:Temps>%/Connect/CPS/DateTime</urn:Temps>
<urn:Emetteur>%/Praticien/PS/ADELI</urn:Emetteur>
<urn:DateRef>%/Connect/CPS/DateTime</urn:DateRef>
<urn:COUVERTURE>
<urn:GrandRegime>%/Patient/Médico_administratif/Code_régime</urn:GrandRegime>
<urn:Organisme>%/Patient/Médico_administratif/Caisse_gestionnaire</urn:Organisme>
<urn:CodeCentre>%/Patient/Médico_administratif/Centre_gestionnaire</urn:CodeCentre>
<urn:ASSURE>
<urn:Id>
<urn:Num>%/Patient/Assuré/Numéro</urn:Num>
<urn:Cle>%/Patient/Assuré/Clé</urn:Cle>
</urn:Id>
</urn:ASSURE>
<urn:BENEFICIAIRE>
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel
<urn:Nir>
<urn:Num>%/Patient/Bénéficiaire/Numéro_individuel</urn:Num>
<urn:Cle>%/Patient/Bénéficiaire/Clé_individuel</urn:Cle>
%#endif
%#ifdef%/Patient/Bénéficiaire/Date_individuel<urn:DateCertification>%/Patient/Bénéficiaire/Date_individuel</urn:DateCertification>%#endif
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel</urn:Nir>%#endif
<urn:DateNai>%/Patient/Bénéficiaire/Date_de_naissance</urn:DateNai>
<urn:Rang>%/Patient/Bénéficiaire/Rang_gémellaire</urn:Rang>
</urn:BENEFICIAIRE>
</urn:COUVERTURE>
</urn:ContexteBAM>
<urn2:ContexteLPS Version="01_00">
<urn2:Id>%/Assertion_ID</urn2:Id>
<urn2:Temps>%/Connect/CPS/DateTime</urn2:Temps>
<urn2:Emetteur>%/Praticien/PS/ADELI</urn2:Emetteur>
<urn2:LPS>
<urn2:IDAM R="4">{EditeurNumName}</urn2:IDAM>
<urn2:Version>{EditeurVersion}</urn2:Version>
<urn2:Instance>%/OID.%/Praticien/PS/ADELI</urn2:Instance>
<urn2:Nom>{EditeurName}</urn2:Nom>
</urn2:LPS>
</urn2:ContexteLPS>
</soap:Header>
<soap:Body>
%#include
</soap:Body>
</soap:Envelope>
        """
        )
        f.close()
    with open("Scripts/ALDbody.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<aff:listerRequest>
<request>
<urn3:Horodatage>%/Connect/CPS/DateTime</urn3:Horodatage>
<urn3:PARTENAIREDESANTE>
<urn4:Numero R="RPPS">%/Praticien/PS/ADELI/1</urn4:Numero>
</urn3:PARTENAIREDESANTE>
<urn3:BENEFICIAIRE>
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel
<urn5:Nir R="NIR">
<urn5:Num>%/Patient/Bénéficiaire/Numéro_individuel</urn5:Num>
<urn5:Cle>%/Patient/Bénéficiaire/Clé_individuel</urn5:Cle>
</urn5:Nir>
%#endif
<urn5:NirOD R="NIROD">
<urn5:Num>%/Patient/Assuré/Numéro</urn5:Num>
<urn5:Cle>%/Patient/Assuré/Clé</urn5:Cle>
</urn5:NirOD>
<urn5:DateNai>%/Patient/Bénéficiaire/Date_de_naissance</urn5:DateNai>
<urn5:Rang>%/Patient/Bénéficiaire/Rang_gémellaire</urn5:Rang>
<urn5:COUVERTURE>
<urn5:GrandRegime>%/Patient/Médico_administratif/Code_régime</urn5:GrandRegime>
<urn5:Organisme>%/Patient/Médico_administratif/Caisse_gestionnaire</urn5:Organisme>
<urn5:EntiteGestion>%/Patient/Médico_administratif/Centre_gestionnaire</urn5:EntiteGestion>
</urn5:COUVERTURE>
</urn3:BENEFICIAIRE>
</request>
</aff:listerRequest>
        """
        )
        f.close()
    #Fonction permettant de switch les checkbox
    done_ald.configure(state=tkinter.NORMAL)
    done_ald.toggle()
    done_ald.configure(state=tkinter.DISABLED)
def button_event_dmt():
    EditeurNumName = entry_ENN.get()
    EditeurVersion = entry_EV.get()
    EditeurName = entry_EN.get()
    with open("Scripts/DMTenv.txt", "w" ,encoding="ANSI") as f:
        f.write(f"""
<?xml version="1.0" encoding="UTF-8" ?>
<soap:Envelope xmlns:cps="http://www.sesam-vitale.fr/XMLschemas/CPS" xmlns:vit="http://www.sesam-vitale.fr/XMLschemas/Vitale" xmlns:dec="http://www.InterRegimes.fr/DeclarationMedecinTraitant" xmlns:urn1="urn:siram:lps:ctxlps" xmlns:urn="urn:siram:bam:ctxbam" xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:add="http://www.w3.org/2005/08/addressing" xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
<soap:Header>
<add:MessageID>%/MessageID</add:MessageID>
<add:Action>urn:MT:2.1.0:TeledeclarerMT</add:Action>
<oas:Security>
%#include/AssertionCPS
%#ifdef%/Vitale%#include/AssertionCV%#endif
</oas:Security>
<urn:ContexteBAM Version="01_02">
<urn:Id>%/Assertion_ID</urn:Id>
<urn:Temps>%/Connect/CPS/DateTime</urn:Temps>
<urn:COUVERTURE>
<urn:GrandRegime>%/Patient/Médico_administratif/Code_régime</urn:GrandRegime>
%#ifdef%/Patient/Médico_administratif/Caisse_gestionnaire<urn:Organisme>%/Patient/Médico_administratif/Caisse_gestionnaire</urn:Organisme>%#endif
%#ifdef%/Patient/Médico_administratif/Centre_gestionnaire<urn:CodeCentre>%/Patient/Médico_administratif/Centre_gestionnaire</urn:CodeCentre>%#endif
<urn:ASSURE>
<urn:Id>
<urn:Num>%/Patient/Assuré/Numéro</urn:Num>
<urn:Cle>%/Patient/Assuré/Clé</urn:Cle>
</urn:Id>
</urn:ASSURE>
<urn:BENEFICIAIRE>
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel
<urn:Nir>
<urn:Num>%/Patient/Bénéficiaire/Numéro_individuel</urn:Num>
<urn:Cle>%/Patient/Bénéficiaire/Clé_individuel</urn:Cle>
%#endif
%#ifdef%/Patient/Bénéficiaire/Date_individuel<urn:DateCertification>%/Patient/Bénéficiaire/Date_individuel</urn:DateCertification>%#endif
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel</urn:Nir>%#endif
<urn:DateNai>%/Patient/Bénéficiaire/Date_de_naissance</urn:DateNai>
<urn:Rang>%/Patient/Bénéficiaire/Rang_gémellaire</urn:Rang>
</urn:BENEFICIAIRE>
</urn:COUVERTURE>
</urn:ContexteBAM>
<urn1:ContexteLPS Nature="CTXLPS" Version="01_00">
<urn1:Id>%/Assertion_ID</urn1:Id>
<urn1:Temps>%/Connect/CPS/DateTime</urn1:Temps>
<urn1:Emetteur>%/Praticien/PS/ADELI</urn1:Emetteur>
<urn1:LPS>
<urn1:IDAM R="4">{EditeurNumName}</urn1:IDAM>
<urn1:Version>{EditeurVersion}</urn1:Version>
<urn1:Instance>%/OID.%/Praticien/PS/ADELI</urn1:Instance>
<urn1:Nom>{EditeurName}</urn1:Nom>
</urn1:LPS>
</urn1:ContexteLPS>
</soap:Header>
<soap:Body>
%#include
</soap:Body>
</soap:Envelope>
        """
        )
        f.close()
    with open("Scripts/DMTbody.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<dec:TeledeclarerMT>
<vit:donneesVitale niveau="01.00">
<vit:carte nature="%/Patient/Médico_administratif/Type_carte"/>
<vit:contratAMO>
<vit:matriculeAssure cle="%/Patient/Assuré/Clé">%/Patient/Assuré/Numéro</vit:matriculeAssure>
<vit:organismeAMO codeCaisse="%/Patient/Médico_administratif/Caisse_gestionnaire" codeRegime="%/Patient/Médico_administratif/Code_régime" codeCentre="%/Patient/Médico_administratif/Centre_gestionnaire"/>
</vit:contratAMO>
<vit:beneficiaire porteur="%/Patient/Bénéficiaire/Porteur">
<vit:identite>
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel
<vit:NIRcertifie dateCertification="%/Patient/Bénéficiaire/Date_individuel" cle="%/Patient/Bénéficiaire/Clé_individuel">%/Patient/Bénéficiaire/Numéro_individuel</vit:NIRcertifie>
%#endif
<vit:nomDetaille prenom="%/Patient/Bénéficiaire/Prénom" nomUsuel="%/Patient/Bénéficiaire/Nom"%#ifdef%/Patient/Bénéficiaire/Nom_naissance nomFamille="%/Patient/Bénéficiaire/Nom_naissance"%#endif/>
<vit:dateNaissance rang="%/Patient/Bénéficiaire/Rang_gémellaire">%/Patient/Bénéficiaire/Date_de_naissance</vit:dateNaissance>
</vit:identite>
</vit:beneficiaire>
</vit:donneesVitale>
<cps:donneesCPS niveau="01.00">
<cps:porteur nomPatronymique="%/Praticien/PS/Nom" prenomUsuel="%/Praticien/PS/Prénom">
<cps:situationExercice>
<cps:situationFacturation>
<cps:identifiantFacturation cle="%/Praticien/PS/Clé">%/Praticien/PS/Numéro</cps:identifiantFacturation>
</cps:situationFacturation>
</cps:situationExercice>
</cps:porteur>
</cps:donneesCPS>
</dec:TeledeclarerMT>
        """
        )
        f.close()
    #Fonction permettant de switch les checkbox
    done_dmt.configure(state=tkinter.NORMAL)
    done_dmt.toggle()
    done_dmt.configure(state=tkinter.DISABLED)
def button_event_imt():
    EditeurNumName = entry_ENN.get()
    EditeurVersion = entry_EV.get()
    EditeurName = entry_EN.get()
    with open("Scripts/IMTenv.txt", "w" ,encoding="ANSI") as f:
        f.write(f"""
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:add="http://www.w3.org/2005/08/addressing" xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:urn="urn:siram:bam:ctxbam" xmlns:urn1="urn:siram:lps:ctxlps" xmlns:urn2="urn:ir:si_reqmt" xmlns:urn3="urn:siram:beneficiaire">
<soap:Header>
<add:MessageID>%/MessageID</add:MessageID>
<add:Action>urn:MT:3.0.0:LireMT</add:Action>
<oas:Security>
%#include/AssertionCPS
%#ifdef%/Vitale%#include/AssertionCV%#endif
</oas:Security>
<urn:ContexteBAM Version="01_02">
<urn:Id>%/Assertion_ID</urn:Id>
<urn:Temps>%/Connect/CPS/UTC</urn:Temps>
<urn:COUVERTURE>
<urn:GrandRegime>%/Patient/Médico_administratif/Code_régime</urn:GrandRegime>
%#ifdef%/Patient/Médico_administratif/Caisse_gestionnaire<urn:Organisme>%/Patient/Médico_administratif/Caisse_gestionnaire</urn:Organisme>%#endif
%#ifdef%/Patient/Médico_administratif/Centre_gestionnaire<urn:CodeCentre>%/Patient/Médico_administratif/Centre_gestionnaire</urn:CodeCentre>%#endif
<urn:ASSURE>
<urn:Id>
<urn:Num>%/Patient/Assuré/Numéro</urn:Num>
<urn:Cle>%/Patient/Assuré/Clé</urn:Cle>
</urn:Id>
</urn:ASSURE>
<urn:BENEFICIAIRE>
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel
<urn:Nir>
<urn:Num>%/Patient/Bénéficiaire/Numéro_individuel</urn:Num>
<urn:Cle>%/Patient/Bénéficiaire/Clé_individuel</urn:Cle>
%#endif
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel</urn:Nir>%#endif
<urn:DateNai>%/Patient/Bénéficiaire/Date_de_naissance</urn:DateNai>
<urn:Rang>%/Patient/Bénéficiaire/Rang_gémellaire</urn:Rang>
</urn:BENEFICIAIRE>
</urn:COUVERTURE>
</urn:ContexteBAM>
<urn1:ContexteLPS Nature="CTXLPS" Version="01_00">
<urn1:Id>%/Assertion_ID</urn1:Id>
<urn1:Temps>%/Connect/CPS/UTC</urn1:Temps>
<urn1:Emetteur>%/Praticien/PS/ADELI</urn1:Emetteur>
<urn1:LPS>
<urn1:IDAM R="4">{EditeurNumName}</urn1:IDAM>
<urn1:Version>{EditeurVersion}</urn1:Version>
<urn1:Instance>%/OID.%/Praticien/PS/ADELI</urn1:Instance>
<urn1:Nom>{EditeurName}</urn1:Nom>
</urn1:LPS>
</urn1:ContexteLPS>
</soap:Header>
<soap:Body>
%#include
</soap:Body>
</soap:Envelope>
        """
        )
        f.close()
    with open("Scripts/IMTbody.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<urn2:SI_REQMT>
<urn2:Temps>%/Connect/CPS/DateTime</urn2:Temps>
<urn2:BENEFICIAIRE>
<urn3:NirOD>
<urn3:Num>%/Patient/Assuré/Numéro</urn3:Num>
<urn3:Cle>%/Patient/Assuré/Clé</urn3:Cle>
</urn3:NirOD>
<urn3:DateNai>%/Patient/Bénéficiaire/Date_de_naissance</urn3:DateNai>
<urn3:RangNai>%/Patient/Bénéficiaire/Rang_gémellaire</urn3:RangNai>
<urn3:COUVERTURE>
<urn3:GrandRegime>%/Patient/Médico_administratif/Code_régime</urn3:GrandRegime>
</urn3:COUVERTURE>
</urn2:BENEFICIAIRE>
</urn2:SI_REQMT>

        """
        )
        f.close()
    #Fonction permettant de switch les checkbox
    done_imt.configure(state=tkinter.NORMAL)
    done_imt.toggle()
    done_imt.configure(state=tkinter.DISABLED)
def button_event_apcv():
    EditeurNumName = entry_ENN.get()
    EditeurVersion = entry_EV.get()
    EditeurName = entry_EN.get()
    with open("Scripts/apCV1env.txt", "w" ,encoding="ANSI") as f:
        f.write(f"""
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:add="http://www.w3.org/2005/08/addressing" xmlns:urn1="urn:siram:lps:ctxlps" xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
<soap:Header>
<add:MessageID>%/MessageID</add:MessageID>
<add:Action>urn:ApCV_AUTH:1.0.0:authentifierUtilisateurProximite</add:Action>
<oas:Security>
%#include/AssertionCPS3
</oas:Security>
<urn1:ContexteLPS Version="01_00">
<urn1:Id>%/Assertion_ID</urn1:Id>
<urn1:Temps>%/Connect/CPS/DateTime</urn1:Temps>
<urn1:Emetteur>%/Praticien/PS/ADELI</urn1:Emetteur>
<urn1:LPS>
<urn1:IDAM R="4">{EditeurNumName}</urn1:IDAM>
<urn1:Version>{EditeurVersion}</urn1:Version>
<urn1:Instance>%/OID.%/Praticien/PS/ADELI</urn1:Instance>
<urn1:Nom>urn:lps:{EditeurName}</urn1:Nom>
</urn1:LPS>
</urn1:ContexteLPS>
</soap:Header>
<soap:Body>
%#include
</soap:Body>
</soap:Envelope>
        """
        )
        f.close()
    with open("Scripts/apCV1body.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<AuthentifierUtilisateurProximiteReq version="1.0" xmlns="http://www.sesam-vitale.fr/apcv/auth/1/0">
<ProfessionnelSante>
<IdentifiantFacturation>%/Praticien/PS/Numéro%/Praticien/PS/Clé</IdentifiantFacturation>
<CodeSpecialiteAMO>%/Praticien/PS/Code_spécialité</CodeSpecialiteAMO>
</ProfessionnelSante>
<Donnees>%#include/qrcode</Donnees>
</AuthentifierUtilisateurProximiteReq>
        """
        )
        f.close()
    with open("Scripts/apCV2env.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:add="http://www.w3.org/2005/08/addressing" xmlns:urn1="urn:siram:lps:ctxlps" xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
<soap:Header>
<add:MessageID>%/MessageID</add:MessageID>
<add:Action>urn:ApCV_AUTH:1.0.0:restituerContexteApCV</add:Action>
<oas:Security>
%#include/AssertionCPS3
</oas:Security>
<urn1:ContexteLPS Version="01_00">
<urn1:Id>%/Assertion_ID</urn1:Id>
<urn1:Temps>%/Connect/CPS/DateTime</urn1:Temps>
<urn1:Emetteur>%/Praticien/PS/ADELI</urn1:Emetteur>
<urn1:LPS>
<urn1:IDAM R="4">{EditeurNumName}</urn1:IDAM>
<urn1:Version>{EditeurVersion}</urn1:Version>
<urn1:Instance>%/OID.%/Praticien/PS/ADELI</urn1:Instance>
<urn1:Nom>urn:lps:{EditeurName}</urn1:Nom>
</urn1:LPS>
</urn1:ContexteLPS>
</soap:Header>
<soap:Body>
%#include
</soap:Body>
</soap:Envelope>
        """
        )
        f.close()
    with open("Scripts/apCV2body.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<RestituerContexteApCVReq version="1.0" xmlns="http://www.sesam-vitale.fr/apcv/auth/1/0"></RestituerContexteApCVReq>
        """
        )
        f.close()
    with open("Scripts/apCV3env.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:add="http://www.w3.org/2005/08/addressing" xmlns:urn1="urn:siram:lps:ctxlps" xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
<soap:Header>
<add:MessageID>%/MessageID</add:MessageID>
<add:Action>urn:ApCV_AUTH:1.0.0:detruireContexteApCV</add:Action>
<oas:Security>
%#include/AssertionCPS3
</oas:Security>
<urn1:ContexteLPS Version="01_00">
<urn1:Id>%/Assertion_ID</urn1:Id>
<urn1:Temps>%/Connect/CPS/DateTime</urn1:Temps>
<urn1:Emetteur>%/Praticien/PS/ADELI</urn1:Emetteur>
<urn1:LPS>
<urn1:IDAM R="4">{EditeurNumName}</urn1:IDAM>
<urn1:Version>{EditeurVersion}</urn1:Version>
<urn1:Instance>%/OID.%/Praticien/PS/ADELI</urn1:Instance>
<urn1:Nom>urn:lps:{EditeurName}</urn1:Nom>
</urn1:LPS>
</urn1:ContexteLPS>
</soap:Header>
<soap:Body>
%#include
</soap:Body>
</soap:Envelope>
        """
        )
        f.close()
    with open("Scripts/apCV3body.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<DetruireContexteApCVReq version="1.0" xmlns="http://www.sesam-vitale.fr/apcv/auth/1/0">
<ContexteApCV>
<Identifiant>%/ECV/Identifiant</Identifiant>
</ContexteApCV>
</DetruireContexteApCVReq>
        """
        )
        f.close()
    with open("Scripts/apCV4env.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:add="http://www.w3.org/2005/08/addressing" xmlns:urn1="urn:siram:lps:ctxlps" xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
<soap:Header>
<add:MessageID>%/MessageID</add:MessageID>
<add:Action>urn:ApCV_SIGN:1.0.0:signerVitale</add:Action>
<oas:Security>
%#include/AssertionCPS3
</oas:Security>
<urn1:ContexteLPS Version="01_00">
<urn1:Id>%/Assertion_ID</urn1:Id>
<urn1:Temps>%/Connect/CPS/DateTime</urn1:Temps>
<urn1:Emetteur>%/Praticien/PS/ADELI</urn1:Emetteur>
<urn1:LPS>
<urn1:IDAM R="4">{EditeurNumName}</urn1:IDAM>
<urn1:Version>{EditeurVersion}</urn1:Version>
<urn1:Instance>%/OID.%/Praticien/PS/ADELI</urn1:Instance>
<urn1:Nom>urn:lps:{EditeurName}</urn1:Nom>
</urn1:LPS>
</urn1:ContexteLPS>
</soap:Header>
<soap:Body>
%#include
</soap:Body>
</soap:Envelope>
        """
        )
        f.close()
    with open("Scripts/apCV4body.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<SignerVitaleReq version="1.0" xmlns="http://www.sesam-vitale.fr/apcv/sign/1/0">
<ContexteApCV><Identifiant>%/ECV/Identifiant</Identifiant></ContexteApCV>
<Facture type="%/ECV/Type">
<NIRAssure cle="%/Patient/Assuré/Clé">%/Patient/Assuré/Numéro</NIRAssure> 
%#ifdef%/ECV4/HachFSE<DonneeFSE>%/ECV4/HachFSE</DonneeFSE>%#endif
%#ifdef%/ECV4/HachDRE<DonneeDRE>%/ECV4/HachDRE</DonneeDRE>%#endif
</Facture>
<ResumeFacture>
<ProfessionnelSante>
<IdentifiantFacturation>%/Praticien/PS/Numéro%/Praticien/PS/Clé</IdentifiantFacturation>
<IdNatPS>%/Praticien/PS/ADELI/1</IdNatPS>
%#ifdef%/PS/Nom_origine<Nom>%/PS/Nom_origine %/PS/Prénom_origine</Nom>
%#else
%#ifdef%/PS/Nom<Nom>%/PS/Nom %/PS/Prénom</Nom>
%#endif
%#endif
</ProfessionnelSante>
<Beneficiaire>
<NomUsage>%/Patient/Bénéficiaire/Nom</NomUsage>
<NomFamille>%/Patient/Bénéficiaire/Nom</NomFamille>
<Prenom>%/Patient/Bénéficiaire/Prénom</Prenom>
<NIRCertifie cle="%/Patient/Bénéficiaire/Clé_individuel">%/Patient/Bénéficiaire/Numéro_individuel</NIRCertifie>
%#include/Amo
%#include/Amc
%#endif
</Beneficiaire>
%#include/Prestation
</ResumeFacture>
</SignerVitaleReq>
        """
        )
        f.close()
        #Fonction permettant de switch les checkbox
    done_apcv.configure(state=tkinter.NORMAL)
    done_apcv.toggle()
    done_apcv.configure(state=tkinter.DISABLED)
def button_event_dre():
    EditeurNumName = entry_ENN.get()
    EditeurVersion = entry_EV.get()
    EditeurName = entry_EN.get()
    with open("Scripts/DREbody.txt", "w" ,encoding="ANSI") as f:
        f.write(f"""
<search xmlns="https://ws.annuaireamc.fr/">
<paramsObj xmlns="">
<requete>
<version>R01</version>
<date_demande>%/Date_demande</date_demande>
<editeur>{EditeurName}</editeur>
<logiciel>{EditeurNumName}</logiciel>
<version_logiciel>{EditeurVersion}</version_logiciel>
</requete>
<adressage>
<numero_amc>%/Patient/Bénéficiaire/Identifiant_AMC</numero_amc>
%#ifdef%/Patient/Bénéficiaire/NumComplEDI/1
<code_type_convention>%/Patient/Bénéficiaire/NumComplEDI/1/2</code_type_convention>
%#endif
%#ifdef%/Patient/Bénéficiaire/NumComplEDI/3
<code_csr>%/Patient/Bénéficiaire/NumComplEDI/3</code_csr>
%#endif
<domaine_conventionnel>%/Domaine</domaine_conventionnel>
<code_service>%/Service</code_service>
<code_norme_service>DRE</code_norme_service>
<version_norme_service>V1.0</version_norme_service>
</adressage>
<typage>
<type_adresse>
<item>MEL</item>
</type_adresse>
</typage>
</paramsObj>
</search>
        """
        )
        f.close()
    with open("Scripts/DREenv.txt", "w" ,encoding="ANSI") as f:
        f.write(f"""
<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
<Body>
%#include
</Body>
</Envelope>
        """)
        f.close()
    #Fonction permettant de switch les checkbox
    done_dre.configure(state=tkinter.NORMAL)
    done_dre.toggle()
    done_dre.configure(state=tkinter.DISABLED)
def button_event_hr():
    EditeurNumName = entry_ENN.get()
    EditeurVersion = entry_EV.get()
    EditeurName = entry_EN.get()
    with open("Scripts/HRenv.txt", "w" ,encoding="ANSI") as f:
        f.write(f"""
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
<soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
<wsa:MessageID>%/MessageID</wsa:MessageID>
<wsa:Action>urn:HR:1.1.0:ConsulterHistorique</wsa:Action>
<wsse:Security>
%#include/AssertionCPS
%#include/AssertionCV
</wsse:Security>
<ctxlps:ContexteLPS Nature="CTXLPS" Version="01_00" xsi:schemaLocation="urn:siram:lps:ctxlps xsd/CTX/ROOT_ctxlps_CTXLPS_V01_00.xsd" xmlns:ctxlps="urn:siram:lps:ctxlps" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<ctxlps:Id>%/Assertion_ID</ctxlps:Id>
<ctxlps:Temps>%/Connect/CPS/UTC</ctxlps:Temps>
<ctxlps:Emetteur>%/Praticien/PS/ADELI</ctxlps:Emetteur>
<ctxlps:LPS>
<ctxlps:IDAM R="4">{EditeurNumName}</ctxlps:IDAM>
<ctxlps:Version>{EditeurVersion}</ctxlps:Version>
<ctxlps:Instance>%/OID.%/Praticien/PS/ADELI</ctxlps:Instance>
<ctxlps:Nom>{EditeurName}</ctxlps:Nom>
</ctxlps:LPS>
</ctxlps:ContexteLPS>
<ctxbam:ContexteBAM Version="01_02" xsi:schemaLocation="urn:siram:bam:ctxbam ../xsd/ctx/ROOT_ctxbam_CTXBAM_V01_02.xsd " Nature="CTXBAM" xmlns:ctxbam="urn:siram:bam:ctxbam" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<ctxbam:Id>%/Assertion_ID</ctxbam:Id>
<ctxbam:Temps>%/Connect/CPS/UTC</ctxbam:Temps>
<ctxbam:Emetteur>%/Praticien/PS/ADELI</ctxbam:Emetteur>
<ctxbam:COUVERTURE>
<ctxbam:GrandRegime>%/Patient/Médico_administratif/Code_régime</ctxbam:GrandRegime>
%#ifdef%/Patient/Médico_administratif/Caisse_gestionnaire<ctxbam:Organisme>%/Patient/Médico_administratif/Caisse_gestionnaire</ctxbam:Organisme>%#endif
%#ifdef%/Patient/Médico_administratif/Centre_gestionnaire<ctxbam:CodeCentre>%/Patient/Médico_administratif/Centre_gestionnaire</ctxbam:CodeCentre>%#endif
<ctxbam:ASSURE>
<ctxbam:Id>
<ctxbam:Num>%/Patient/Assuré/Numéro</ctxbam:Num>
<ctxbam:Cle>%/Patient/Assuré/Clé</ctxbam:Cle>
</ctxbam:Id>
</ctxbam:ASSURE>
<ctxbam:BENEFICIAIRE>
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel
<ctxbam:Nir>
<ctxbam:Num>%/Patient/Bénéficiaire/Numéro_individuel</ctxbam:Num>
<ctxbam:Cle>%/Patient/Bénéficiaire/Clé_individuel</ctxbam:Cle>
%#endif
%#ifdef%/Patient/Bénéficiaire/Date_individuel<ctxbam:DateCertification>%/Patient/Bénéficiaire/Date_individuel</ctxbam:DateCertification>%#endif
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel</ctxbam:Nir>%#endif
<ctxbam:DateNai>%/Patient/Bénéficiaire/Date_de_naissance</ctxbam:DateNai>
<ctxbam:Rang>%/Patient/Bénéficiaire/Rang_gémellaire</ctxbam:Rang>
</ctxbam:BENEFICIAIRE>
</ctxbam:COUVERTURE>
</ctxbam:ContexteBAM>
</soap:Header>
<soap:Body>
%#body
</soap:Body>
</soap:Envelope>
            """)
        f.close()
    with open("Scripts/HRall.txt", "w" ,encoding="ANSI") as f:
        f.write(f"""
<hr:ConsulterHistorique xmlns:hr="http://www.InterRegimes.fr/HR5" xmlns:curmed="http://www.InterRegimes.fr/namespace/EXP/0/0" xmlns:cps="http://www.sesam-vitale.fr/XMLschemas/CPS" xmlns:client="http://www.sesam-vitale.fr/XMLschemas/Client" xmlns:vitale="http://www.sesam-vitale.fr/XMLschemas/Vitale" xmlns:env="http://www.w3.org/2003/05/soap-envelope">
<curmed:RequetePersonne PGMD_Version="1.4" PGMD_Profil="WPSREQ" Profil_Version="1.7">
<curmed:Date>%/Connect/CPS/DateTime/0/10</curmed:Date>
<curmed:Fonction>%/Médico_administratif/Fonction_carte</curmed:Fonction>
<curmed:Sujet>
<curmed:Certificat>
<curmed:Objet>
<curmed:Code>AM</curmed:Code>
</curmed:Objet>
<curmed:Objet>
<curmed:Code>RD</curmed:Code>
</curmed:Objet>
<curmed:Objet>
<curmed:Code>LB</curmed:Code>
</curmed:Objet>
<curmed:Objet>
<curmed:Code>OF</curmed:Code>
</curmed:Objet>
<curmed:Objet>
<curmed:Code>CP</curmed:Code>
</curmed:Objet>
<curmed:Objet>
<curmed:Code>TR</curmed:Code>
</curmed:Objet>
<curmed:Objet>
<curmed:Code>IJ</curmed:Code>
</curmed:Objet>
<curmed:Validite>
<curmed:Debut>%/Periode_debut</curmed:Debut>
<curmed:Fin>%/Connect/CPS/DateTime/0/10</curmed:Fin>
</curmed:Validite>
</curmed:Certificat>
</curmed:Sujet>
</curmed:RequetePersonne>
<vitale:donneesVitale niveau="01.00">
<vitale:carte nature="%/Patient/Médico_administratif/Type_carte"/>
<vitale:contratAMO>
<vitale:matriculeAssure cle="%/Patient/Assuré/Clé">%/Patient/Assuré/Numéro</vitale:matriculeAssure>
<vitale:organismeAMO codeCaisse="%/Patient/Médico_administratif/Caisse_gestionnaire" codeCentre="%/Patient/Médico_administratif/Centre_gestionnaire" codeRegime="%/Patient/Médico_administratif/Code_régime"/>
</vitale:contratAMO>
<vitale:beneficiaire porteur="%/Patient/Bénéficiaire/Porteur">
<vitale:identite>
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel
<vitale:NIRcertifie dateCertification="%/Patient/Bénéficiaire/Date_individuel" cle="%/Patient/Bénéficiaire/Clé_individuel">%/Patient/Bénéficiaire/Numéro_individuel</vitale:NIRcertifie>
%#endif
<vitale:nomDetaille prenom="%/Patient/Bénéficiaire/Prénom" nomUsuel="%/Patient/Bénéficiaire/Nom"%#ifdef%/Patient/Bénéficiaire/Nom_naissance nomFamille="%/Patient/Bénéficiaire/Nom_naissance"%#endif/>
<vitale:dateNaissance rang="%/Patient/Bénéficiaire/Rang_gémellaire">%/Patient/Bénéficiaire/Date_de_naissance</vitale:dateNaissance>
</vitale:identite>
</vitale:beneficiaire>
</vitale:donneesVitale>
<cps:donneesCPS niveau="01.00">
<cps:porteur nomPatronymique="%/Praticien/PS/Nom" prenomUsuel="%/Praticien/PS/Prénom">
<cps:caracteristiquesNationales>
<cps:identifiantNational type="%/Praticien/PS/ADELI/0/1">%/Praticien/PS/ADELI/1</cps:identifiantNational>
</cps:caracteristiquesNationales>
</cps:porteur>
</cps:donneesCPS>
</hr:ConsulterHistorique>
            """)
        f.close()
    #Fonction permettant de switch les checkbox
    done_hr.configure(state=tkinter.NORMAL)
    done_hr.toggle()
    done_hr.configure(state=tkinter.DISABLED)
def button_event_inss():
    EditeurNumName = entry_ENN.get()
    EditeurVersion = entry_EV.get()
    EditeurName = entry_EN.get()
    with open("Scripts/INSSenv.txt", "w" ,encoding="ANSI") as f:
        f.write(f"""
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:add="http://www.w3.org/2005/08/addressing" xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:urn="urn:siram:bam:ctxbam" xmlns:urn1="urn:siram:lps:ctxlps" xmlns:ins="http://www.cnamts.fr/INSiRecSans">
<soap:Header>
<add:MessageID>uuid:%/MessageID</add:MessageID>
<add:Action>urn:ServiceIdentiteCertifiee:1.0.0:rechercherInsAvecTraitsIdentite</add:Action>
<oas:Security>
%#include/AssertionCPS4
</oas:Security>
<urn:ContexteBAM Version="01_02">
<urn:Id>%/HL7Id</urn:Id>
<urn:Temps>%/Connect/CPS/UTC</urn:Temps>
<urn:Emetteur>%/Praticien/PS/ADELI</urn:Emetteur>
<urn:COUVERTURE/>
</urn:ContexteBAM>
<urn1:ContexteLPS Version="01_00">
<urn1:Id>%/HL7queryId</urn1:Id>
<urn1:Temps>%/Connect/CPS/UTC</urn1:Temps>
<urn1:Emetteur>%/Praticien/PS/ADELI</urn1:Emetteur>
<urn1:LPS>
<urn1:IDAM R="4">{EditeurNumName}</urn1:IDAM>
<urn1:Version>{EditeurVersion}</urn1:Version>
<urn1:Instance>%/OID.%/Praticien/PS/ADELI</urn1:Instance>
<urn1:Nom>urn:lps:{EditeurName}</urn1:Nom>
</urn1:LPS>
</urn1:ContexteLPS>
</soap:Header>
<soap:Body>
%#include
</soap:Body>
</soap:Envelope>
        """)
        f.close()
    with open("Scripts/INSSbody.txt", "w" ,encoding="ANSI") as f:
        f.write(f"""
<ins:RECSANSVITALE>
<ins:NomNaissance>%/Nom</ins:NomNaissance>
<ins:Prenom>%/Prenom</ins:Prenom>
<ins:Sexe>%/Sexe</ins:Sexe>
<ins:DateNaissance>%/Date_de_naissance</ins:DateNaissance>
%#ifdef%/Lieu_de_naissance
<ins:LieuNaissance>%/Lieu_de_naissance</ins:LieuNaissance>
%#endif
</ins:RECSANSVITALE>

        """)
        f.close()
    #Fonction permettant de switch les checkbox
    done_inss.configure(state=tkinter.NORMAL)
    done_inss.toggle()
    done_inss.configure(state=tkinter.DISABLED)
def button_event_insv():
    EditeurNumName = entry_ENN.get()
    EditeurVersion = entry_EV.get()
    EditeurName = entry_EN.get()
    with open("Scripts/INSVenv.txt", "w" ,encoding="ANSI") as f:
        f.write(f"""
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:add="http://www.w3.org/2005/08/addressing" xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:urn="urn:siram:bam:ctxbam" xmlns:urn1="urn:siram:lps:ctxlps" xmlns:ins="http://www.cnamts.fr/INSiRecVit">
<soap:Header>
<add:MessageID>uuid:%/MessageID</add:MessageID>
<add:Action>urn:ServiceIdentiteCertifiee:1.0.0:rechercherInsAvecCarteVitale</add:Action>
<oas:Security>
%#include/AssertionCPS4
%#ifdef%/Vitale%#include/AssertionCV%#endif
</oas:Security>
<urn:ContexteBAM Version="01_02">
<urn:Id>%/HL7Id</urn:Id>
<urn:Temps>%/Connect/CPS/UTC</urn:Temps>
<urn:Emetteur>%/Praticien/PS/ADELI</urn:Emetteur>
<urn:COUVERTURE>
<urn:ASSURE>
<urn:Id>
<urn:Num>%/Patient/Assuré/Numéro</urn:Num>
</urn:Id>
</urn:ASSURE>
<urn:BENEFICIAIRE>
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel
<urn:Nir>
<urn:Num>%/Patient/Bénéficiaire/Numéro_individuel</urn:Num>
</urn:Nir>
%#endif
<urn:DateNai>%/Patient/Bénéficiaire/Date_de_naissance</urn:DateNai>
<urn:Rang>%/Patient/Bénéficiaire/Rang_gémellaire</urn:Rang>
</urn:BENEFICIAIRE>
</urn:COUVERTURE>
</urn:ContexteBAM>
<urn1:ContexteLPS Version="01_00">
<urn1:Id>%/HL7queryId</urn1:Id>
<urn1:Temps>%/Connect/CPS/UTC</urn1:Temps>
<urn1:Emetteur>%/Praticien/PS/ADELI</urn1:Emetteur>
<urn1:LPS>
<urn1:IDAM R="4">{EditeurNumName}</urn1:IDAM>
<urn1:Version>{EditeurVersion}</urn1:Version>
<urn1:Instance>%/OID.%/Praticien/PS/ADELI</urn1:Instance>
<urn1:Nom>urn:lps:{EditeurName}</urn1:Nom>
</urn1:LPS>
</urn1:ContexteLPS>
</soap:Header>
<soap:Body>
%#include
</soap:Body>
</soap:Envelope>
        """)
        f.close()
    with open("Scripts/INSVbody.txt", "w" ,encoding="ANSI") as f:
        f.write(f"""
<ins:RECVITALE>
%#ifdef%/Patient/Bénéficiaire/Numéro_individuel
<ins:MatriculeIndividu>
<ins:NumIdentifiant>%/Patient/Bénéficiaire/Numéro_individuel</ins:NumIdentifiant>
</ins:MatriculeIndividu>
%#endif
<ins:MatriculeOD>
<ins:NumIdentifiant>%/Patient/Assuré/Numéro</ins:NumIdentifiant>
</ins:MatriculeOD>
%#ifdef%/Bénéficiaire/Nom_naissance
<ins:NomNaissance>%/Bénéficiaire/Nom_naissance</ins:NomNaissance>
%#else
%#ifdef%/Patient/Assuré/Nom_naissance
<ins:NomNaissance>%/Patient/Assuré/Nom_naissance</ins:NomNaissance>
%#endif
%#endif
<ins:DateNaissance>%/Patient/Bénéficiaire/Date_de_naissance</ins:DateNaissance>
<ins:RangNaissance>%/Patient/Bénéficiaire/Rang_gémellaire</ins:RangNaissance>
</ins:RECVITALE>
        """)
        f.close()
    #Fonction permettant de switch les checkbox
    done_insv.configure(state=tkinter.NORMAL)
    done_insv.toggle()
    done_insv.configure(state=tkinter.DISABLED)

def ini_gen():
    with open("Pyxvital.ini", "w", encoding="ANSI") as f:
        f.write(pyx_ini)
        f.close()
    with open("Pyxvital.ini", "a", encoding="ANSI") as f: #Section [SCOR]Modifie certif.tab et ajoute les certifs si coché, si non les retires (en cas d'erreur)
        if cb_ini1.get() == "on":
            print("function on")
            f.write(scor)
            with open("Certificats/Certificats.tab","w",encoding="UTF-8") as fc:
                fc.write(certif_scor)
                fc.close()
            path_scor = glob.glob("Certificats/scor_der/*.scor.rss.fr.der")
            for file in path_scor:
                shutil.move(file,"Certificats/")
        else :
            print("function off")
            path_certif_scor = glob.glob("Certificats/*.scor.rss.fr.der")
            for file in path_certif_scor:
                if os.path.exists(file):
                    shutil.move(file,"Certificats/scor_der")
                else:
                    print("path not exist --- " + file)
                    continue
            with open("Certificats/Certificats.tab","w",encoding="UTF-8") as fc:
                fc.write(certif_ss_scor)
                fc.close()
            
        if cb_ini2.get() == "on":
            f.write(aldi)
        else :
            pass
        if cb_ini3.get() == "on":
            f.write(dmti)
        else :
            pass
        if cb_ini4.get() == "on":
            f.write(imti)
        else :
            pass
        if cb_ini5.get() == "on":
            f.write(hri)
        else :
            pass
        if cb_ini6.get() == "on":
            f.write(apcv)
        else :
            pass
        if cb_ini7.get() == "on":
            f.write(insi)
        else :
            pass
        if cb_ini8.get() == "on":
            f.write(srt)
        else :
            pass

def until_exit():
    if os.path.exists("Certificats/scor_der"):
        path_scor = glob.glob("Certificats/scor_der/*.scor.rss.fr.der")
        for file in path_scor:
                os.remove(file)
        os.rmdir("Certificats/scor_der")
    else:
        print("Dossier 'scor_der' introuvable")

def app_on():
    if os.path.exists("Certificats/scor_der"):
        path_scor = glob.glob("Certificats/scor_der/*.scor.rss.fr.der")
        for file in path_scor:
                os.remove(file)
        os.rmdir("Certificats/scor_der")
    else:
        os.mkdir("Certificats/scor_der")
        if os.path.exists("Certificats/scor_der"):
            path_certif_scor = glob.glob("Certificats/*.scor.rss.fr.der")
            for file in path_certif_scor:
                shutil.move(file,"Certificats/scor_der")

def set_filename():
    files = filedialog.askopenfilenames(parent=app,initialdir=r"T:/")
    path = list(files)
    list_of_path = path
    return list_of_path


#_____________________________________Lancement de l'application___________________________________________________________________#
app_on() #Déplacer les fichiers de certificats dans un dossier "scor_der" (le crée si il existe pas)
#__________________________________________________________________________________________________________________________________#
#FIRST FRAME OF THE APP
main_frame = customtkinter.CTkFrame(
    master=app,
    width = 910,
    height = 710,
    corner_radius = 5,
    )
main_frame.pack(padx=10, pady=10)

#P* IMG OF TITLE - TITLE OF APP#
Pyx_img = Image.open(r"assets/pyx_title.png")
title_pyx_img = ImageTk.PhotoImage(Pyx_img)
label_title_img = tkinter.Label(
    image = title_pyx_img, 
    bg = "#2A2D2E",
)
label_title_img.place(x=290,y=15)

#OPTION MENU - OPEN FOLDER PATH ON SELECTION#
win_opt_menu = customtkinter.CTkOptionMenu(
    master = app,
    values = win_editeur_list,
    command = optionmenu_callback,
    dynamic_resizing = False,
    width = 150,
    )
win_opt_menu.place(x=530,y=110)
win_opt_menu.set("Editeurs WIN")

multi_opt_menu = customtkinter.CTkOptionMenu(
    master = app,
    values = multi_editeur_list,
    command = optionmenu_callback,
    dynamic_resizing = False,
    width = 150,
    )
multi_opt_menu.place(x=530,y=150)
multi_opt_menu.set("Editeurs Multi-OS")

osx_opt_menu = customtkinter.CTkOptionMenu(
    master = app,
    values = osx_editeur_list,
    command = optionmenu_callback,
    dynamic_resizing = False,
    width = 150,
    )
osx_opt_menu.place(x=730,y=110)
osx_opt_menu.set("Editeurs OSX")

linux_opt_menu = customtkinter.CTkOptionMenu(
    master = app,
    values = linux_editeur_list,
    command = optionmenu_callback,
    dynamic_resizing = False,
    width = 150,
    )
linux_opt_menu.place(x=730,y=150)
linux_opt_menu.set("Editeurs LINUX")

ios_opt_menu = customtkinter.CTkOptionMenu(
    master = app,
    values = ios_editeur_list,
    command = optionmenu_callback,
    dynamic_resizing = False,
    width = 150,
    )
ios_opt_menu.place(x=530,y=190)
ios_opt_menu.set("Editeurs IOS")

socle_tech_menu = customtkinter.CTkOptionMenu(
    master = app,
    fg_color = "#c92e48",
    button_color = "#961e32",
    button_hover_color = "#751626",
    values = socle_technique_list,
    command = optionmenu_callback,
    dynamic_resizing = False,
    width = 150,
    )
socle_tech_menu.place(x=730,y=190)
socle_tech_menu.set("Socle Technique")

#FRAME INSID THE MAIN_FRAME#
frame_2 = customtkinter.CTkFrame(
    master=main_frame,
    width = 370,
    height = 455,
    corner_radius = 5,
    )
frame_2.place(x=517.5,y=235)
#ENTRY FOR VARIABLE OF CREATING .TXT#
l1 = customtkinter.CTkLabel(
    master = app,
    width = 115,
    height = 30,
    bg_color = "#343638",
    text = "N° d'autorisation",
)
l1.place(x=530,y=245)
entry_ENN = customtkinter.CTkEntry(
    master = app,
    width = 115,
    height = 30,
    placeholder_text="N° d'autorisation",
)
entry_ENN.place(x=535,y=275)

l2 = customtkinter.CTkLabel(
    master = app,
    width = 115,
    height = 30,
    bg_color = "#343638",
    text = "Nom editeur",
)
l2.place(x=635,y=245)
entry_EN = customtkinter.CTkEntry(
    master = app,
    width = 115,
    height = 30,
    placeholder_text="Nom editeur",
)
entry_EN.place(x=655,y=275)

l3 = customtkinter.CTkLabel(
    master = app,
    width = 115,
    height = 30,
    bg_color = "#343638",
    text = "Version editeur",
)
l3.place(x=765,y=245)
entry_EV = customtkinter.CTkEntry(
    master = app,
    width = 115,
    height = 30,
    placeholder_text="Version editeur",
)
entry_EV.place(x=775,y=275)

#LINE#
label_line = customtkinter.CTkLabel(
    master = app,
    width = 115,
    height = 30,
    bg_color = "#343638",
    text = "______________________________________________________",
)
label_line.place(x=550,y=305)

#BUTTON AND VALIDATING CHECKBOX FOR FUNCTION CREATING .TXT#
#BUTTON LIST : ADR - ALD - DMT - IMT - APCV - DRE - HR - INSS - INSV

button_adr = customtkinter.CTkButton(
    master = app,
    text = "ADRenv.txt",
    width= 230,
    command = button_event_adr,
)
button_adr.place(x=535,y=345)

done_adr = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_adr.place(x=780,y=345)

button_ald = customtkinter.CTkButton(
    master = app,
    text = "ALDenv.txt",
    width= 230,
    command = button_event_ald,
)
button_ald.place(x=535,y=385)

done_ald = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_ald.place(x=780,y=385)

button_dmt = customtkinter.CTkButton(
    master = app,
    text = "DMTenv.txt",
    width= 230,
    command = button_event_dmt,
)
button_dmt.place(x=535,y=425)

done_dmt = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_dmt.place(x=780,y=425)

button_imt = customtkinter.CTkButton(
    master = app,
    text = "IMTenv.txt",
    width= 230,
    command = button_event_imt,
)
button_imt.place(x=535,y=465)

done_imt = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_imt.place(x=780,y=465)

button_apcv = customtkinter.CTkButton(
    master = app,
    text = "APCVenv.txt",
    width= 230,
    command = button_event_apcv,
)
button_apcv.place(x=535,y=505)

done_apcv = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_apcv.place(x=780,y=505)

button_dre = customtkinter.CTkButton(
    master = app,
    text = "DREbody.txt",
    width= 230,
    command = button_event_dre,
)
button_dre.place(x=535,y=545)

done_dre = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_dre.place(x=780,y=545)

button_hr = customtkinter.CTkButton(
    master = app,
    text = "HRenv.txt",
    width= 230,
    command = button_event_hr,
)
button_hr.place(x=535,y=585)

done_hr = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_hr.place(x=780,y=585)

button_inss = customtkinter.CTkButton(
    master = app,
    text = "INSSenv.txt",
    width= 230,
    command = button_event_inss,
)
button_inss.place(x=535,y=625)

done_inss = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_inss.place(x=780,y=625)

button_insv = customtkinter.CTkButton(
    master = app,
    text = "INSVenv.txt",
    width= 230,
    command = button_event_insv,
)
button_insv.place(x=535,y=665)

done_insv = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_insv.place(x=780,y=665)


#______________________________________CATEGORIE TRANSFERT__________________________________#
#Certificat + checkbox validate
#CCAMbis + checkbox validate
#Table_v2.srt + checkbox validate
#______________________________________CERTIFICAT__________________________________#
tr_titre1_label = customtkinter.CTkLabel(
    master = app,
    width = 435,
    height = 25,
    text = "Transfert des certificats",
    bg_color = "#2a2d2e",
    text_font = ("Arial", 13)
)
tr_titre1_label.place(x=10, y=105)

certif_frame = customtkinter.CTkFrame(
    master = main_frame,
    height = 105,
    width = 440,
)
certif_frame.place(x=10, y=120)

tr_certificat1_label = customtkinter.CTkLabel(
    master = app,
    width = 135,
    height = 25,
    text = None,
)
tr_certificat1_label.place(x=25, y=165)

tr_certificat1_button = customtkinter.CTkButton(
    master = app,
    text = "Parcourir...",
    width = 135,
    command = set_filename,
)
tr_certificat1_button.place(x=25, y=135)

cl1 = customtkinter.CTkLabel(
    master = app,
    width = 115,
    height = 30,
    bg_color = "#343638",
    text = "►►",
    text_color = "#FFFFFF",
    text_font = ("ARIAL",20)
)
cl1.place(x=160, y=135)

tr_certificat2_label = customtkinter.CTkLabel(
    master = app,
    width = 135,
    height = 25,
    text = None,
)
tr_certificat2_label.place(x=265, y=165)

tr_certificat2_button = customtkinter.CTkButton(
    master = app,
    text = "Parcourir...",
    width = 135,
    command = set_filename,
)
tr_certificat2_button.place(x=265, y=135)

tr_certificat1_validCheck = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    height = 25,
    width = 25,
)
tr_certificat1_validCheck.place(x=420, y=197)

tr_certificatBIG1_button = customtkinter.CTkButton(
    master = app,
    text = "Transférer...",
    width = 380,
)
tr_certificatBIG1_button.place(x=25, y=195)

#______________________________________TABLE_V2__________________________________#
tr_titre2_label = customtkinter.CTkLabel(
    master = app,
    width = 435,
    height = 25,
    text = "Transfert Table_v2.srt",
    bg_color = "#2a2d2e",
    text_font = ("Arial", 13)
)
tr_titre2_label.place(x=10, y=245)

certif_frame = customtkinter.CTkFrame(
    master = main_frame,
    height = 105,
    width = 440,
)
certif_frame.place(x=10, y=260)

tr_certificat3_label = customtkinter.CTkLabel(
    master = app,
    width = 135,
    height = 25,
    text = None,
)
tr_certificat3_label.place(x=25, y=305)

tr_certificat3_button = customtkinter.CTkButton(
    master = app,
    text = "Parcourir...",
    width = 135,
    command = set_filename,
)
tr_certificat3_button.place(x=25, y=275)

cl1 = customtkinter.CTkLabel(
    master = app,
    width = 115,
    height = 30,
    bg_color = "#343638",
    text = "►►",
    text_color = "#FFFFFF",
    text_font = ("ARIAL",20)
)
cl1.place(x=160, y=285)

tr_certificat4_label = customtkinter.CTkLabel(
    master = app,
    width = 135,
    height = 25,
    text = None,
)
tr_certificat4_label.place(x=265, y=305)

tr_certificat4_button = customtkinter.CTkButton(
    master = app,
    text = "Parcourir...",
    width = 135,
    command = set_filename,
)
tr_certificat4_button.place(x=265, y=275)

tr_certificat2_validCheck = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    height = 25,
    width = 25,
)
tr_certificat2_validCheck.place(x=420, y=337)

tr_certificatBIG2_button = customtkinter.CTkButton(
    master = app,
    text = "Transférer...",
    width = 380,
)
tr_certificatBIG2_button.place(x=25, y=335)

#______________________________________CCAMbis__________________________________#
tr_titre3_label = customtkinter.CTkLabel(
    master = app,
    width = 435,
    height = 25,
    text = "Transfert CCAMbis",
    bg_color = "#2a2d2e",
    text_font = ("Arial", 13)
)
tr_titre3_label.place(x=10, y=385)

certif_frame = customtkinter.CTkFrame(
    master = main_frame,
    height = 105,
    width = 440,
)
certif_frame.place(x=10, y=400)

tr_certificat5_label = customtkinter.CTkLabel(
    master = app,
    width = 135,
    height = 25,
    text = None,
)
tr_certificat5_label.place(x=25, y=445)

tr_certificat5_button = customtkinter.CTkButton(
    master = app,
    text = "Parcourir...",
    width = 135,
    command = set_filename,
)
tr_certificat5_button.place(x=25, y=415)

cl1 = customtkinter.CTkLabel(
    master = app,
    width = 115,
    height = 30,
    bg_color = "#343638",
    text = "►►",
    text_color = "#FFFFFF",
    text_font = ("ARIAL",20)
)
cl1.place(x=160, y=425)

tr_certificat6_label = customtkinter.CTkLabel(
    master = app,
    width = 135,
    height = 25,
    text = None,
)
tr_certificat6_label.place(x=265, y=445)

tr_certificat6_button = customtkinter.CTkButton(
    master = app,
    text = "Parcourir...",
    width = 135,
    command = set_filename,
)
tr_certificat6_button.place(x=265, y=415)

tr_certificat3_validCheck = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    height = 25,
    width = 25,
)
tr_certificat3_validCheck.place(x=420, y=477)

tr_certificatBIG3_button = customtkinter.CTkButton(
    master = app,
    text = "Transférer...",
    width = 380,
    
)
tr_certificatBIG3_button.place(x=25, y=475)


#_________________________________________CHECKBOX INI____________________________________________#

cb_ini1 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"[SCOR]", 
    onvalue="on", offvalue="off",
    )
cb_ini1.place(x=20,y=520)

cb_ini2 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"[ALDi]", 
    onvalue="on", offvalue="off",
    )
cb_ini2.place(x=20,y=550)

cb_ini3 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"[DMTi]", 
    onvalue="on", offvalue="off",
    )
cb_ini3.place(x=20,y=580)

cb_ini4 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"[IMTi]", 
    onvalue="on", offvalue="off",
    )
cb_ini4.place(x=20,y=610)

cb_ini5 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"[HRi]", 
    onvalue="on", offvalue="off",
    )
cb_ini5.place(x=250,y=520)

cb_ini6 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"[ECVx] → APCV", 
    onvalue="on", offvalue="off",
    )
cb_ini6.place(x=250,y=550)

cb_ini7 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"[INSi]", 
    onvalue="on", offvalue="off",
    )
cb_ini7.place(x=250,y=580)

cb_ini8 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"[SRT] + Outrepasse=CC8", 
    onvalue="on", offvalue="off",
    )
cb_ini8.place(x=250,y=610)

ini_button = customtkinter.CTkButton(
    master = main_frame,
    width = 430,
    fg_color = "#c92e48",
    hover_color = "#751626",
    text = r"Générer Pyxvital.ini",
    command = ini_gen,

)
ini_button.place(x=20,y=650)






#MAINLOOP AND RESIZE-OPTIONS#

atexit.register(until_exit) #lancement de la fonction lorsqu'on quitte l'appli
app.resizable(False,False)
app.mainloop()
