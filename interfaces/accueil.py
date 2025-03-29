import customtkinter

from fonctions.fonctions_accueil import page


def afficherPageAccueil(app,nomUser):
    frame = customtkinter.CTkFrame(app,width=1920,height=580)
    frame.place(relx=0.5, rely=1, anchor="s")
    page(app,frame,nomUser)