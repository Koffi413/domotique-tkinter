import customtkinter

from controllers import requete_utilisateurs as bd
from fonctions.fonctions_glob import suivant

bullet = "\u2022"
def creer(app,frameForm,nomUser,mdpUser,crea):
    nom = nomUser.get()
    mdp = mdpUser.get()
    insert = bd.ajouterUtilisateurs(nom, mdp)
    if insert:
        suiv = customtkinter.CTkButton(app, text="Suivant", text_color="white", width=200, height=40,command=lambda: suivant(app, suiv, frameForm,crea,None))
        suiv.place(x=1050, y=590)

def afficher_mdp(btn_oeil_mdp,champMdp,oeil_ouvert,oeil_ferme):
    if champMdp.cget("show") == bullet:
       btn_oeil_mdp.configure(image=oeil_ouvert)
       champMdp.configure(show="")
    else:
       champMdp.configure(show=bullet)
       btn_oeil_mdp.configure(image=oeil_ferme)

def afficher_conf(btn_oeil_conf,champConf,oeil_ouvert,oeil_ferme):
    if champConf.cget("show") == bullet:
       btn_oeil_conf.configure(image=oeil_ouvert)
       champConf.configure(show="")
    else:
        champConf.configure(show=bullet)
        btn_oeil_conf.configure(image=oeil_ferme)

def etats(root,creation,btn_oeil_mdp,champMdp,btn_oeil_conf,mess,champConf,nomUser,mdpUser,confMdp):
    nom = nomUser.get()
    mdp = mdpUser.get()
    conf = confMdp.get()
    if len(mdp) > 0:
        btn_oeil_mdp.place(in_=champMdp, relx=1, rely=0.5, anchor="e")
    if len(conf) > 0:
        btn_oeil_conf.place(in_=champConf, relx=1, rely=0.5, anchor="e")

    if nom != "" and mdp != "" and conf != "":
       if mdp == conf:
          mess.place_forget()
          creation.configure(state="normal")
          creation.configure(fg_color="#0d6efd")
          creation.configure(hover_color="#3f8cfd")
          root.after(3000, mess.place_forget)
       else:
          mess.configure(text="Les deux mots de passe sont différents", text_color="#ffc107")
          mess.cget("font").configure(size=12)
          mess.place(x=280, y=310)
    else:
       creation.configure(state="disabled")

