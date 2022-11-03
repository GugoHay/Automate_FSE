import tkinter
import customtkinter
from PIL import Image, ImageTk
import os
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
    with open("ADRenv.txt", "w", encoding="ANSI") as f:
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
    with open("ADRbody.txt", "w", encoding="ANSI") as f:
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
    with open("ALDenv.txt", "w" ,encoding="ANSI") as f:
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
    with open("ALDbody.txt", "w", encoding="ANSI") as f:
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
    with open("DMTenv.txt", "w" ,encoding="ANSI") as f:
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
    with open("DMTbody.txt", "w", encoding="ANSI") as f:
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
    with open("IMTenv.txt", "w" ,encoding="ANSI") as f:
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
    with open("IMTbody.txt", "w", encoding="ANSI") as f:
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
    with open("apCV1env.txt", "w" ,encoding="ANSI") as f:
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
    with open("apCV1body.txt", "w", encoding="ANSI") as f:
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
    with open("apCV2env.txt", "w", encoding="ANSI") as f:
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
    with open("apCV2body.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<RestituerContexteApCVReq version="1.0" xmlns="http://www.sesam-vitale.fr/apcv/auth/1/0"></RestituerContexteApCVReq>
        """
        )
        f.close()
    with open("apCV3env.txt", "w", encoding="ANSI") as f:
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
    with open("apCV3body.txt", "w", encoding="ANSI") as f:
        f.write(f"""
<DetruireContexteApCVReq version="1.0" xmlns="http://www.sesam-vitale.fr/apcv/auth/1/0">
<ContexteApCV>
<Identifiant>%/ECV/Identifiant</Identifiant>
</ContexteApCV>
</DetruireContexteApCVReq>
        """
        )
        f.close()
    with open("apCV4env.txt", "w", encoding="ANSI") as f:
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
    with open("apCV4body.txt", "w", encoding="ANSI") as f:
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
    with open("DREbody.txt", "w" ,encoding="ANSI") as f:
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
    with open("DREenv.txt", "w" ,encoding="ANSI") as f:
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
    with open("HRenv.txt", "w" ,encoding="ANSI") as f:
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
    with open("HRall.txt", "w" ,encoding="ANSI") as f:
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
    with open("INSSenv.txt", "w" ,encoding="ANSI") as f:
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
    with open("INSSbody.txt", "w" ,encoding="ANSI") as f:
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
    with open("INSVenv.txt", "w" ,encoding="ANSI") as f:
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
    with open("INSVbody.txt", "w" ,encoding="ANSI") as f:
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
    onvalue="on", offvalue="off"
    )
cb_ini1.place(x=20,y=520)

cb_ini2 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"[ALDi]", 
    onvalue="on", offvalue="off"
    )
cb_ini2.place(x=20,y=550)

cb_ini3 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"[INSi]", 
    onvalue="on", offvalue="off"
    )
cb_ini3.place(x=20,y=580)

cb_ini4 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"Numéro_FSE_fin=999999", 
    onvalue="on", offvalue="off"
    )
cb_ini4.place(x=20,y=610)

cb_ini5 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"[SRT] + Outrepasse=CC8", 
    onvalue="on", offvalue="off"
    )
cb_ini5.place(x=250,y=520)

cb_ini6 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"Garder_pendant=090", 
    onvalue="on", offvalue="off"
    )
cb_ini6.place(x=250,y=550)

cb_ini7 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"Verif_Formules_STS=N", 
    onvalue="on", offvalue="off"
    )
cb_ini7.place(x=250,y=580)

cb_ini8 = customtkinter.CTkCheckBox(
    master=main_frame, 
    text=r"VersionPatient.par=1", 
    onvalue="on", offvalue="off"
    )
cb_ini8.place(x=250,y=610)

ini_button = customtkinter.CTkButton(
    master = main_frame,
    width = 430,
    text = r"Générer Pyxvital.ini"

)
ini_button.place(x=20,y=650)

#append des parties de l'ini quand les checkbox sont True ça devrait le faire :)

#MAINLOOP AND RESIZE-OPTIONS#
app.resizable(False,False)
app.mainloop()
