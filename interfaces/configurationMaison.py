import tkinter

import customtkinter
from fonctions.fonctions_config_maison import activeValide
from fonctions.fonctions_glob import suivant


def afficherPageConfig(app,nomUser):
    nomMaison = customtkinter.StringVar()
    nomPiece = customtkinter.StringVar()
    typePiece = customtkinter.IntVar(value=0)
    superficiePiece = customtkinter.StringVar()
    superficiePiece.set("0")

    frameConfig = customtkinter.CTkFrame(app, width=1100, height=600)
    frameConfig.place(relx=0.55,rely=0.45,anchor="center")
    titre = customtkinter.CTkLabel(frameConfig,text="Configurations")
    titre.cget("font").configure(size=30)
    titre.place(x=7,y=7)
    #formulaire ajout de pieces
    labMais = customtkinter.CTkLabel(frameConfig, text="Nommez vôtre maison:")
    labMais.place(x=15,y=100)
    champMais = customtkinter.CTkEntry(frameConfig,textvariable=nomMaison, width=400, height=30)
    champMais.place(x=250, y=100)
    labPiece= customtkinter.CTkLabel(frameConfig, text="Nom de la pièce:")
    labPiece.place(x= 15, y=180)
    champPiece = customtkinter.CTkEntry(frameConfig,textvariable=nomPiece, width=400,height=30)
    champPiece.place(x=180, y=180)

    labType = customtkinter.CTkLabel(frameConfig, text="Type de pièce:")
    labType.place(x=15, y=260)
    salon = customtkinter.CTkRadioButton(frameConfig, text="Salon", variable= typePiece, value=1)
    salon.place(x=180,y=260)
    chambre = customtkinter.CTkRadioButton(frameConfig, text="Chambre", variable= typePiece, value=2)
    chambre.place(x=300,y=260)
    cuisine = customtkinter.CTkRadioButton(frameConfig, text="Cuisine", variable= typePiece, value=3)
    cuisine.place(x=460,y=260)
    salbain = customtkinter.CTkRadioButton(frameConfig, text="Salle de bain", variable= typePiece, value=4)
    salbain.place(x=580,y=260)
    labSuperficie = customtkinter.CTkLabel(frameConfig,text="Superficie (m²):")
    labSuperficie.place(x=15,y=340)
    champSuperficie = customtkinter.CTkEntry(frameConfig,textvariable=superficiePiece, width=60,justify="center")
    champSuperficie.place(x=180, y=340)
    btnValid = customtkinter.CTkButton(frameConfig,text="Valider", width=80,height=30,text_color="white", fg_color="#D9D9D9",hover_color="#D9D9D9")
    btnValid.place(x=300,y =380)
    btnAjout = customtkinter.CTkButton(frameConfig,text="Ajouter une autre pièce", width=100,height=30,text_color="white",fg_color="#D9D9D9",hover_color="#D9D9D9")
    btnAjout.place(x=450,y =380)
    suiv = customtkinter.CTkButton(app, text="Suivant", text_color="white", width=200, height=40,command=lambda: suivant(app, suiv, frameConfig, None,nomMaison.get(),None))
    nomMaison.trace("w",lambda *args: activeValide(app,btnValid,nomMaison,nomPiece,typePiece,superficiePiece,btnAjout,champMais,champPiece,suiv,frameConfig,nomUser))
    nomPiece.trace("w",lambda *args:activeValide(app,btnValid, nomMaison, nomPiece, typePiece, superficiePiece,btnAjout,champMais,champPiece,suiv,frameConfig,nomUser))
    typePiece.trace("w",lambda *args:activeValide(app,btnValid, nomMaison,nomPiece, typePiece, superficiePiece,btnAjout,champMais,champPiece,suiv,frameConfig,nomUser))
    superficiePiece.trace("w",lambda *args:activeValide(app,btnValid, nomMaison, nomPiece, typePiece, superficiePiece,btnAjout,champMais,champPiece,suiv,frameConfig,nomUser))