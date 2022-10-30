import tkinter
import customtkinter
from PIL import Image, ImageTk
import doc_tls
import os
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("920x720")
app.title("Package Creator")
app.iconbitmap("assets\image_12.ico")

#VARIABLES#
EditeurNumName = "xxxxxxxx"
EditeurVersion = ""
EditeurName = ""

#FUNCTIONS#
def optionmenu_callback(choice):
    if choice == "Medimust":
        os.startfile(r"C:\Users\Gugo\Desktop\editeurs\Medimust")
    elif choice == "Varimed":
        os.startfile(r"C:\Users\Gugo\Desktop\editeurs\Varimed")
    elif choice == "Visiodent":
        os.startfile(r"C:\Users\Gugo\Desktop\editeurs\Visiodent")

def button_event_adr():
        with open("ADRenv.txt", "w" ,encoding="ANSI") as f:
            f.write(doc_tls.tls["ADR"])
            f.close()
            #Fonction permettant de switch les checkbox
            done_adr.configure(state=tkinter.NORMAL)
            done_adr.toggle()
            done_adr.configure(state=tkinter.DISABLED)
def button_event_ald():
        with open("ALDenv.txt", "w" ,encoding="ANSI") as f:
            f.write(doc_tls.tls["ALD"])
            f.close()
            #Fonction permettant de switch les checkbox
            done_ald.configure(state=tkinter.NORMAL)
            done_ald.toggle()
            done_ald.configure(state=tkinter.DISABLED)
def button_event_dmt():
        with open("DMTenv.txt", "w" ,encoding="ANSI") as f:
            f.write(doc_tls.tls["DMT"])
            f.close()
            #Fonction permettant de switch les checkbox
            done_dmt.configure(state=tkinter.NORMAL)
            done_dmt.toggle()
            done_dmt.configure(state=tkinter.DISABLED)
def button_event_imt():
        with open("IMTenv.txt", "w" ,encoding="ANSI") as f:
            f.write(doc_tls.tls["IMT"])
            f.close()
            #Fonction permettant de switch les checkbox
            done_imt.configure(state=tkinter.NORMAL)
            done_imt.toggle()
            done_imt.configure(state=tkinter.DISABLED)
def button_event_apcv():
        with open("APCVenv.txt", "w" ,encoding="ANSI") as f:
            f.write(doc_tls.tls["APCV"])
            f.close()
            #Fonction permettant de switch les checkbox
            done_apcv.configure(state=tkinter.NORMAL)
            done_apcv.toggle()
            done_apcv.configure(state=tkinter.DISABLED)
def button_event_dre():
        with open("DREbody.txt", "w" ,encoding="ANSI") as f:
            f.write(doc_tls.tls["DRE"])
            f.close()
            #Fonction permettant de switch les checkbox
            done_dre.configure(state=tkinter.NORMAL)
            done_dre.toggle()
            done_dre.configure(state=tkinter.DISABLED)
def button_event_hr():
        with open("HRenv.txt", "w" ,encoding="ANSI") as f:
            f.write(doc_tls.tls["HR"])
            f.close()
            #Fonction permettant de switch les checkbox
            done_hr.configure(state=tkinter.NORMAL)
            done_hr.toggle()
            done_hr.configure(state=tkinter.DISABLED)
def button_event_inss():
        with open("INSSenv.txt", "w" ,encoding="ANSI") as f:
            f.write(doc_tls.tls["INSS"])
            f.close()
            #Fonction permettant de switch les checkbox
            done_inss.configure(state=tkinter.NORMAL)
            done_inss.toggle()
            done_inss.configure(state=tkinter.DISABLED)
def button_event_insv():
        with open("INSVenv.txt", "w" ,encoding="ANSI") as f:
            f.write(doc_tls.tls["INSV"])
            f.close()
            #Fonction permettant de switch les checkbox
            done_insv.configure(state=tkinter.NORMAL)
            done_insv.toggle()
            done_insv.configure(state=tkinter.DISABLED)

#FIRST FRAME OF THE APP
main_frame = customtkinter.CTkFrame(
    master=app,
    width = 910,
    height = 710,
    corner_radius = 5,
    )
main_frame.pack(padx=10, pady=10)

#P* IMG OF TITLE - TITLE OF APP#
Pyx_img = Image.open(r"assets\pyx_title.png")
title_pyx_img = ImageTk.PhotoImage(Pyx_img)
label_title_img = tkinter.Label(
    image = title_pyx_img, 
    bg = "#2A2D2E",
)
label_title_img.place(x=290,y=15)

#OPTION MENU - OPEN FOLDER PATH ON SELECTION#
editeur_opt_menu = customtkinter.CTkOptionMenu(
    master=app,
    values=["Medimust", "Varimed","Visiodent"],
    command=optionmenu_callback,
    )
editeur_opt_menu.place(x=730,y=35)
editeur_opt_menu.set("Liste des éditeurs")
#FRAME INSID THE MAIN_FRAME#
frame_2 = customtkinter.CTkFrame(
    master=main_frame,
    width = 370,
    height = 405,
    corner_radius = 5,
    )
frame_2.place(x=517.5,y=90)
#ENTRY FOR VARIABLE OF CREATING .TXT#
    #EditeurNumName
    #EditeurVersion
    #EditeurName
entry_ENN = customtkinter.CTkEntry(
    master = app,
    width = 115,
    height = 30,
    placeholder_text="N° d'autorisation",
)
entry_ENN.place(x=535,y=105)

entry_EN = customtkinter.CTkEntry(
    master = app,
    width = 115,
    height = 30,
    placeholder_text="Nom Editeur",
)
entry_EN.place(x=655,y=105)

entry_EV = customtkinter.CTkEntry(
    master = app,
    width = 115,
    height = 30,
    placeholder_text="Version Editeur",
)
entry_EV.place(x=775,y=105)

#BUTTON AND VALIDATING CHECKBOX FOR FUNCTION CREATING .TXT#
#BUTTON LIST : ADR - ALD - DMT - IMT - APCV - DRE - HR - INSS - INSV

button_adr = customtkinter.CTkButton(
    master = app,
    text = "ADRenv.txt",
    width= 230,
    command = button_event_adr,
)
button_adr.place(x=535,y=150)

done_adr = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_adr.place(x=780,y=150)

button_ald = customtkinter.CTkButton(
    master = app,
    text = "ALDenv.txt",
    width= 230,
    command = button_event_ald,
)
button_ald.place(x=535,y=190)

done_ald = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_ald.place(x=780,y=190)

button_dmt = customtkinter.CTkButton(
    master = app,
    text = "DMTenv.txt",
    width= 230,
    command = button_event_dmt,
)
button_dmt.place(x=535,y=230)

done_dmt = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_dmt.place(x=780,y=230)

button_imt = customtkinter.CTkButton(
    master = app,
    text = "IMTenv.txt",
    width= 230,
    command = button_event_imt,
)
button_imt.place(x=535,y=270)

done_imt = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_imt.place(x=780,y=270)

button_apcv = customtkinter.CTkButton(
    master = app,
    text = "APCVenv.txt",
    width= 230,
    command = button_event_apcv,
)
button_apcv.place(x=535,y=310)

done_apcv = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_apcv.place(x=780,y=310)

button_dre = customtkinter.CTkButton(
    master = app,
    text = "DREbody.txt",
    width= 230,
    command = button_event_dre,
)
button_dre.place(x=535,y=350)

done_dre = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_dre.place(x=780,y=350)

button_hr = customtkinter.CTkButton(
    master = app,
    text = "HRenv.txt",
    width= 230,
    command = button_event_hr,
)
button_hr.place(x=535,y=390)

done_hr = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_hr.place(x=780,y=390)

button_inss = customtkinter.CTkButton(
    master = app,
    text = "INSSenv.txt",
    width= 230,
    command = button_event_inss,
)
button_inss.place(x=535,y=430)

done_inss = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_inss.place(x=780,y=430)

button_insv = customtkinter.CTkButton(
    master = app,
    text = "INSVenv.txt",
    width= 230,
    command = button_event_insv,
)
button_insv.place(x=535,y=470)

done_insv = customtkinter.CTkCheckBox(
    master = app,
    hover = False,
    state = tkinter.DISABLED, #CHECKBOX IS UNCLICKABLE
    text = None,
    bg_color = "#343638",
    width= 100,
)
done_insv.place(x=780,y=470)

#MAINLOOP AND RESIZE-OPTIONS#
app.resizable(False,False)
app.mainloop()