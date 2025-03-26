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
    frameForm.pack(expand=True)
    formTitre = customtkinter.CTkLabel(frameForm, text="Compte Personnel", font=("Lota Grotesque", 40))
    formTitre.place(x=20, y=20)
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
    btn_oeil_mdp = customtkinter.CTkButton(frameForm, text="", image=oeil_ferme, command= lambda :afficher_mdp(champMdp,oeil_ouvert,oeil_ferme,btn_oeil_mdp), width=10)
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
    creation = customtkinter.CTkButton(app, text="Créer compte", text_color="white", width=400, height=40,
                                       command=lambda: creer(suiv,nomUser,mdpUser))
    creation.place(x=450, y=500)
    # boutonsuivant
    suiv = customtkinter.CTkButton(app, text="Suivant", text_color="white", width=200, height=40,command=lambda: suivant(app))
    suiv.place_forget()
    # Progression
    framePro = customtkinter.CTkFrame(app, width=1250, height=58, fg_color="white")
    framePro.pack(side="bottom")
    # etape
    barreCompte = customtkinter.CTkFrame(framePro, width=450, height=10, corner_radius=0)
    barreCompte.place(x=0, y=0)
    etapeCompte = customtkinter.CTkLabel(framePro, text="Création de compte", )
    etapeCompte.cget("font").configure(size=25)
    etapeCompte.place(x=100, y=15)
    barreConf = customtkinter.CTkFrame(framePro, width=450, height=10, corner_radius=0)
    barreConf.place(x=450, y=0)
    etapeConf = customtkinter.CTkLabel(framePro, text="Configuration de la maison", )
    etapeConf.cget("font").configure(size=25)
    etapeConf.place(x=520, y=15)
    barreFin = customtkinter.CTkFrame(framePro, width=450, height=10, corner_radius=0)
    barreFin.place(x=900, y=0)
    etapeFin = customtkinter.CTkLabel(framePro, text="Terminé")
    etapeFin.cget("font").configure(size=25)
    etapeFin.place(x=1050, y=15)
    etats(app,creation,btn_oeil_mdp,champMdp,btn_oeil_conf,mess,barreCompte,etapeCompte,etapeFin,etapeConf,barreFin,barreConf,champConf,nomUser,mdpUser,confMdp)
    nomUser.trace("w", lambda *args: etats(app,creation,btn_oeil_mdp,champMdp,btn_oeil_conf,mess,barreCompte,etapeCompte,etapeFin,etapeConf,barreFin,barreConf,champConf,nomUser,mdpUser,confMdp))
    mdpUser.trace("w", lambda *args: etats(app,creation,btn_oeil_mdp,champMdp,btn_oeil_conf,mess,barreCompte,etapeCompte,etapeFin,etapeConf,barreFin,barreConf,champConf,nomUser,mdpUser,confMdp))
    confMdp.trace("w", lambda *args: etats(app,creation,btn_oeil_mdp,champMdp,btn_oeil_conf,mess,barreCompte,etapeCompte,etapeFin,etapeConf,barreFin,barreConf,champConf,nomUser,mdpUser,confMdp))


