import customtkinter

from fonctions.fonctions_accueil import page, iconReglage, iconUser
from fonctions.fonctions_glob import deconnexion


def afficherPageAccueil(app,nomUser):
    frame = customtkinter.CTkFrame(app,width=1920,height=580,fg_color="transparent")
    frame.place(relx=0.5, rely=1, anchor="s")
    titre = customtkinter.CTkLabel(app, font=('Lota Grotesque', 60, 'bold', 'underline'))
    page(nomUser,titre)
    btnSalon = customtkinter.CTkButton(frame,text="Salons",width=150,height=150)
    btnSalon.place(relx=0.4, rely=0.1, anchor="n")
    btnCuisine=customtkinter.CTkButton(frame,text="Cuisines",width=150,height=150)
    btnCuisine.place(relx=0.4, rely=0.8, anchor="s")
    btnChambre=customtkinter.CTkButton(frame,text="Chambres",width=150,height=150)
    btnChambre.place(relx=0.6, rely=0.1, anchor="n")
    btnSalBain = customtkinter.CTkButton(frame, text="Salles de bain", width=150, height=150)
    btnSalBain.place(relx=0.6, rely=0.8, anchor="s")
    iconReg = customtkinter.CTkButton(frame, text="Paramètres    ",hover_color="#D9D9D9",fg_color="#D9D9D9", image=iconReglage,text_color="black")
    iconReg.place( relx=0.8, rely=0.4, anchor="e")
    iconUsers = customtkinter.CTkButton(frame, text="Déconnexion", image=iconUser, width=20, text_color="#FA5252",hover_color="#D9D9D9",fg_color="#D9D9D9",command=lambda :deconnexion(app,frame,titre))
    iconUsers.place(relx=0.8, rely=0.5, anchor="e")