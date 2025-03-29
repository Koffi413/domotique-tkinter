import customtkinter

from controllers.requete_maisons import trouverMaison


def page(app,frame,nom):
    maisonUser = trouverMaison(nom)
    titre = customtkinter.CTkLabel(app,text=maisonUser[0][0].upper(),font=('Lota Grotesque',60,'bold','underline'))
    titre.place(relx=0.5,rely=0.1, anchor='center')