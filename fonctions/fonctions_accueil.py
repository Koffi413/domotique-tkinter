import customtkinter
from  PIL import Image

from controllers.requete_maisons import trouverMaison
from controllers.requete_pieces import listeTypePiece
from fonctions.fonctions_glob import vider_frame, retour
eclairage =0

iconReglage = customtkinter.CTkImage(light_image=Image.open("icons/reglage.png"), size=(20,20))
iconUser= customtkinter.CTkImage(light_image=Image.open("icons/user.png"), size=(20,20))
iconAdd = customtkinter.CTkImage(light_image=Image.open("icons/add.png"), size=(20,20))
iconAccueil = customtkinter.CTkImage(light_image=Image.open("icons/accueil.png"), size=(20,20))
iconRetour = customtkinter.CTkImage(light_image=Image.open("icons/retour.png"), size=(20,20))
iconModifier = customtkinter.CTkImage(light_image=Image.open("icons/modifier.png"), size=(20,20))
iconAmpoule_on = customtkinter.CTkImage(light_image=Image.open("icons/ampoule_on.png"), size=(200,200))
iconAmpoule_off = customtkinter.CTkImage(light_image=Image.open("icons/ampoule_off.png"), size=(200,200))
iconEteint = customtkinter.CTkImage(light_image=Image.open("icons/eteint.png"), size=(100,100))
iconAllume = customtkinter.CTkImage(light_image=Image.open("icons/allume.png"), size=(100,100))

def page(nom,titre):
    maisonUser = trouverMaison(nom)
    titre.configure(text=maisonUser[0][0].upper())
    titre.place(relx=0.5,rely=0.1, anchor='center')


def typePieces(frame,nomMaison,type,app,nomUser):
    piece = listeTypePiece(nomMaison.lower(),type)
    if len(piece) > 0:
        vider_frame(frame)
        btnAjout = customtkinter.CTkButton(frame, text="Ajouter une autre pièce", image=iconAdd,text_color="black", fg_color="transparent",hover=False)
        btnAjout.place(relx=0.8,rely=0.3, anchor='e')
        btnAccueil = customtkinter.CTkButton(frame, text="Accueil", image=iconAccueil, text_color="black",fg_color="transparent",hover=False, command=lambda: retour(app, nomUser, frame))
        btnAccueil.place(relx=0.8, rely=0.4, anchor='e')
        relx = 0.4
        if len(piece)>6:
            rely = 0.1
        else:
            rely = 0.2
        for i in range(len(piece)):
            typePiece = customtkinter.CTkLabel(frame,text=f"{type}(s)".upper())
            typePiece.cget("font").configure(size=35)
            typePiece.place(relx=0.2,rely=0.5, anchor='w')
            btnPiece = customtkinter.CTkButton(frame, text=piece[i][0], width=150, height=150,command=lambda: gererPiece(frame,piece[i],nomUser,app))
            btnPiece.place(relx=relx, rely=rely, anchor="n")
            if i ==2:
                relx = 0.4
                rely = rely+0.3
            else:
                relx = relx+0.1



def gererPiece(frame,piece,nomUser,app):
    vider_frame(frame)
    retours = customtkinter.CTkButton(frame, text="Retour",image=iconRetour,command=lambda :typePieces(frame,piece[3],piece[2],app,nomUser),fg_color="transparent",hover=False,text_color="black")
    retours.place(relx=0.2, rely=0.3, anchor='w')
    btnAjout = customtkinter.CTkButton(frame, text="Renommer", image=iconModifier, text_color="black",fg_color="transparent", hover=False)
    btnAjout.place(relx=0.8, rely=0.3, anchor='e')
    btnAccueil = customtkinter.CTkButton(frame, text="Accueil", image=iconAccueil, text_color="black",fg_color="transparent", hover=False,command=lambda: retour(app, nomUser, frame))
    btnAccueil.place(relx=0.8, rely=0.4, anchor='e')
    if eclairage ==1:
        etat = iconAmpoule_on
        interup = iconAllume
        texte = "Éteindre"
    else:
        etat = iconAmpoule_off
        interup = iconEteint
        texte = "Allumer"

    ampoule = customtkinter.CTkButton(frame,text="Eclairage", image=etat, text_color="black",fg_color="transparent", hover=False,compound="bottom")
    ampoule.place(relx=0.6, rely=0.5, anchor='center')
    interrupteur = customtkinter.CTkButton(frame,text=texte, image=interup, text_color="black",fg_color="transparent", hover=False,compound="top",command=lambda :lumiere(ampoule,interrupteur))
    interrupteur.place(relx=0.6, rely=0.8, anchor='center')
def lumiere(ampoule,bouton):
    global eclairage
    if eclairage ==1:
        ampoule.configure(image=iconAmpoule_on)
        bouton.configure(image=iconAllume)
        bouton.configure(text="Éteindre")
        eclairage=0
    else:
        ampoule.configure(image=iconAmpoule_off)
        bouton.configure(image=iconEteint)
        bouton.configure(text="Allumer")
        eclairage=1