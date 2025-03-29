import customtkinter
from PIL import Image

from fonctions.fonctions_connexion import afficher_mdp, bullet, connect, etat


def afficherPageConnexion(app):
    oeil_ouvert = customtkinter.CTkImage(light_image=Image.open("icons/ouvert.png"), size=(20, 20))
    oeil_ferme = customtkinter.CTkImage(light_image=Image.open("icons/fermé.png"), size=(20, 20))
    # formulaire de connexion
    nomUser = customtkinter.StringVar()
    mdpUser = customtkinter.StringVar()
    frameForm = customtkinter.CTkFrame(app, width=700, height=300)
    frameForm.place(relx=0.5, rely=0.5, anchor="center")
    formTitre = customtkinter.CTkLabel(frameForm, text="Connexion", font=("Lota Grotesque", 40))
    formTitre.place(relx=0.5, rely=0.05, anchor="n")
    formNom = customtkinter.CTkLabel(frameForm, text="Nom utilisateur :", )
    formNom.place(x=20, y=120)
    champNom = customtkinter.CTkEntry(frameForm, textvariable=nomUser, width=350, height=30)
    app.update()
    champNom.focus_set()
    champNom.cget("font").configure(size=17)
    champNom.place(x=180, y=120)
    formMdp = customtkinter.CTkLabel(frameForm, text="Mot de passe :")
    formMdp.place(x=20, y=200)
    champMdp = customtkinter.CTkEntry(frameForm, textvariable=mdpUser, width=350, height=30, show=bullet)
    champMdp.place(x=180, y=200)
    btn_oeil_mdp = customtkinter.CTkButton(frameForm, text="", image=oeil_ferme,command=lambda: afficher_mdp(btn_oeil_mdp, champMdp, oeil_ouvert,oeil_ferme), width=10)
    btn_oeil_mdp.configure(fg_color="white")
    btn_oeil_mdp.configure(hover_color="white")
    btn_oeil_mdp.place_forget()
    # boutoncréation
    connexion = customtkinter.CTkButton(app, text="Se connecter", text_color="white", width=400, height=40,command=lambda: connect(app,nomUser, mdpUser,),fg_color="#D9D9D9", hover_color="#D9D9D9")
    connexion.place(relx=0.5, rely=0.78, anchor="s")
    nomUser.trace("w",lambda *args: etat(connexion, btn_oeil_mdp, champMdp, nomUser,mdpUser))
    mdpUser.trace("w",lambda *args: etat(connexion, btn_oeil_mdp, champMdp,nomUser,mdpUser))

