import customtkinter

from fonctions.fonctions_accueil import page, iconReglage, iconUser, typePieces, iconSalon, iconCuisine, iconChambre, \
    iconBain
from fonctions.fonctions_glob import deconnexion


def afficherPageAccueil(app,nomUser):
    frame = customtkinter.CTkFrame(app,width=1920,height=580,fg_color="transparent")
    frame.place(relx=0.5, rely=1, anchor="s")
    titre = customtkinter.CTkLabel(app, font=('Lota Grotesque', 60, 'bold', 'underline'))
    page(nomUser,titre)
    btnSalon = customtkinter.CTkButton(frame,text="Salons",image=iconSalon,command=lambda :typePieces(frame,titre.cget("text"),"Salon",app,nomUser),compound="top",fg_color="transparent",hover=False,text_color="black")
    btnSalon.place(relx=0.4, rely=0.1, anchor="n")
    btnCuisine=customtkinter.CTkButton(frame,text="Cuisines",image=iconCuisine,command=lambda :typePieces(frame,titre.cget("text"),"Cuisine",app,nomUser),compound="top",fg_color="transparent",hover=False,text_color="black")
    btnCuisine.place(relx=0.4, rely=0.8, anchor="s")
    btnChambre=customtkinter.CTkButton(frame,text="Chambres",image=iconChambre,command=lambda :typePieces(frame,titre.cget("text"),"Chambre",app,nomUser),compound="top",fg_color="transparent",hover=False,text_color="black")
    btnChambre.place(relx=0.6, rely=0.1, anchor="n")
    btnSalBain = customtkinter.CTkButton(frame, text="Salles de bain",image=iconBain,command=lambda :typePieces(frame,titre.cget("text"),"Salle de Bain",app,nomUser),compound="top",fg_color="transparent",hover=False,text_color="black")
    btnSalBain.place(relx=0.6, rely=0.8, anchor="s")
    iconReg = customtkinter.CTkButton(frame, text="Paramètres    ",hover=False,fg_color="transparent", image=iconReglage,text_color="black")
    iconReg.place( relx=0.8, rely=0.4, anchor="e")
    iconUsers = customtkinter.CTkButton(frame, text="Déconnexion", image=iconUser,text_color="#FA5252",hover=False,fg_color="transparent",command=lambda :deconnexion(app,frame,titre))
    iconUsers.place(relx=0.8, rely=0.5, anchor="e")
