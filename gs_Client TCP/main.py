import socket
import tkinter
from tkinter import *
import customtkinter
import atexit


app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
app.title('Client TCP')
app.geometry('450x350')

#| HOST = 'localhost'  #| Nom / ip  serveur
#| PORT = 5050         #| Même port que le serveur


crlf = b"\r\n.\r\n"       #| <CRLF>.<CRLF> (pour avoir les retours de pyx)

combobox_var = customtkinter.StringVar(value="TEST://") #Valeur initiale 
check_var = tkinter.StringVar(value="off")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



#____________________________________FUNCTIONS___________________________________#
def conn():
    
    HOST = entry_host.get()         #| On récupère la variable dans l'entrée "Adresse IP"
    PORT = int(entry_port.get())    #| On récupère la variable dans l'entrée "Port" (type : Int)
    
    if checkbox_conn.get() == 'on':

        textbox_return.configure(state="normal")        #|
        textbox_return.delete('0.0','end')              #|-> Vide la textbox
        textbox_return.configure(state="disable")       #|
        try:
            #| Connexion directement au socket, variable host et port
            s.connect((HOST,PORT))

            textbox_return.configure(state="normal")
            textbox_return.insert("0.0","Connexion au serveur " + '"' + HOST + ':' + str(PORT)+ '"' + " avec succès")
            textbox_return.configure(state="disable")
            #| On précise dans la textbox que la connexion à été effectuer lorsque celui-ci
            #| est connecter au socket
            print("Connecter au serveur TCP" + ' ' + HOST + ':' + str(PORT))
            
        except:
            #| On renvoie une erreur avec le nom et le port du réseaux lorsque celui-ci
            #| est innexistant (information dans la textbox)
            textbox_return.configure(state="normal")
            textbox_return.insert("0.0","Le serveur " + '"' + HOST + ':' + str(PORT) + '"' + " est introuvable.. ")
            textbox_return.configure(state="disable")
            print("Serveur" + ' ' + HOST + ':' + str(PORT) + "introuvable")
    elif checkbox_conn.get() == 'off':
        
        textbox_return.configure(state="normal")        #|
        textbox_return.delete('0.0','end')              #|-> Vide la textbox
        textbox_return.configure(state="disable")       #|

        s.close()    #| Ferme le socket
        s.__init__() #| Reinitialise le socket à chaque appel de la fonction

        textbox_return.configure(state="normal")        #|
        textbox_return.insert(0.0,'Déconnecter')        #|-> Informe de la déconnexion
        textbox_return.configure(state="disable")       #|
        #| On ne check pas si le client est connecter ou non au socket,
        #| on ferme le socket quoi qu'il arrive et on le reinitialise
        print("Déconnecter du serveur TCP" + ' ' + HOST + ':' + str(PORT))

def send():

    textbox_return.configure(state="normal")            #|
    textbox_return.delete('0.0','end')                  #|-> Vide la textbox
    textbox_return.configure(state="disable")           #|

    cmd = bytes(combobox_cmd.get(), encoding='ANSI') + crlf    #| Encodage de la commande en bytes + Ajout du crlf en bytes
    s.sendall(cmd)                                             #| Envoie de la commande

    data = s.recv(20480)                                       #| Reception des données par Pyx

    textbox_return.configure(state="normal")
    textbox_return.insert(0.0,data.decode('ANSI'))      #| Ecriture des données dans le textbox
    textbox_return.configure(state="disable")

def atclosure():
    s.close()       #| Fermeture socket à la fermeture de l'app

#____________________________________TKINTER____________________________________#


label1 = customtkinter.CTkLabel(master=app, text="Adresse IP :")
label1.place(x=0,y=5)

entry_host = customtkinter.CTkEntry(
    master=app,
    placeholder_text="Adresse IP :",
    width=120,
    height=25,
    border_width=2,
    corner_radius=10,
    textvariable='')
entry_host.place(x=25,y=30)
entry_host.insert(0,'localhost')    #| Valeur par défaut du champ d'entré

label2 = customtkinter.CTkLabel(master=app, text="Port :")
label2.place(x=180,y=5)

entry_port = customtkinter.CTkEntry(
    master=app,
    placeholder_text="Port :",
    width=120,
    height=25,
    border_width=2,
    corner_radius=10,
    textvariable='')
entry_port.place(x=225,y=30)
entry_port.insert(0,'50')           #| Valeur par défaut du champ d'entré

checkbox_conn = customtkinter.CTkCheckBox(
    master=app, 
    width=20,
    height=20,
    text="Connexion..",
    variable=check_var,
    onvalue="on", 
    offvalue="off",
    command=conn)
checkbox_conn.place(x=25,y=75)

combobox_cmd = customtkinter.CTkComboBox(
    master=app,
    width = 260,
    values=["TEST://", "EXECSHOW://", "EXECHIDE://", "READ://", "WRITE://"],
    variable=combobox_var)
combobox_cmd.place(x=25,y=120)

# checkbox_crlf = customtkinter.CTkCheckBox(
#     master=app, 
#     width=20,
#     height=20,
#     text="Ajouter <CRLF>.<CRLF>",)
# checkbox_crlf.grid(column=0,row=3,padx=5,pady=5)

button_send = customtkinter.CTkButton (text = "Envoyer",command=send)
button_send.place(x=300,y=120)

textbox_return = Text(
    master= app,
    width = 50,
    height = 10,)
textbox_return.place(x=25,y=170)
textbox_return.configure(state="disable")  #| Bloque la textbox pour éviter l'écriture à l'interieur par l'utilisateur



atexit.register(atclosure)  #| A la fermeture de l'app, ferme le socket.
app.focus_force()
app.resizable(False,False)
app.mainloop()

