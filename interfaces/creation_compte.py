import customtkinter
from fonctions.fonctions_creation_compte import etats,afficher_mdp,afficher_conf,creer,bullet
from fonctions.fonctions_glob import suivant
from PIL import Image


def afficherPageCompte(app):
    oeil_ouvert = customtkinter.CTkImage(light_image=Image.open("icons/ouvert.png"), size=(20, 20))
    oeil_ferme = customtkinter.CTkImage(light_image=Image.open("icons/fermé.png"), size=(20, 20))
    # formulaire de connexion
    nomUser = customtkinter.StringVar()
    mdpUser = customtkinter.StringVar()
    confMdp = customtkinter.StringVar()
    frameForm = customtkinter.CTkFrame(app, width=800, height=350)
    frameForm.place(relx=0.5, rely=0.5, anchor="center")
    formTitre = customtkinter.CTkLabel(frameForm, text="Compte Personnel", font=("Lota Grotesque", 40))
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
    btn_oeil_mdp = customtkinter.CTkButton(frameForm, text="", image=oeil_ferme, command= lambda :afficher_mdp(btn_oeil_mdp,champMdp,oeil_ouvert,oeil_ferme), width=10)
    btn_oeil_mdp.configure(fg_color="white")
    btn_oeil_mdp.configure(hover_color="white")
    btn_oeil_mdp.place_forget()
    formConf = customtkinter.CTkLabel(frameForm, text="Confirmez mot de passe :")
    formConf.place(x=20, y=280)
    champConf = customtkinter.CTkEntry(frameForm, textvariable=confMdp, width=350, height=30, show=bullet)
    champConf.place(x=280, y=280)
    btn_oeil_conf = customtkinter.CTkButton(frameForm, text="", image=oeil_ferme, command=lambda :afficher_conf(btn_oeil_conf,champConf,oeil_ouvert,oeil_ferme), width=10)
    btn_oeil_conf.configure(fg_color="white")
    btn_oeil_conf.configure(hover_color="white")
    btn_oeil_conf.place_forget()
    # Label message (caché au début)
    mess = customtkinter.CTkLabel(frameForm, text="", text_color="#ffc107")
    mess.place_forget()
    # boutoncréation
    creation = customtkinter.CTkButton(app, text="Créer compte", text_color="white", width=400, height=40,command=lambda: creer(app,frameForm,nomUser,mdpUser,creation),fg_color="#D9D9D9",hover_color="#D9D9D9")
    creation.place(relx=0.5, rely=0.81, anchor="s")
    nomUser.trace("w", lambda *args: etats(app,creation,btn_oeil_mdp,champMdp,btn_oeil_conf,mess,champConf,nomUser,mdpUser,confMdp))
    mdpUser.trace("w", lambda *args: etats(app,creation,btn_oeil_mdp,champMdp,btn_oeil_conf,mess,champConf,nomUser,mdpUser,confMdp))
    confMdp.trace("w", lambda *args: etats(app,creation,btn_oeil_mdp,champMdp,btn_oeil_conf,mess,champConf,nomUser,mdpUser,confMdp))

