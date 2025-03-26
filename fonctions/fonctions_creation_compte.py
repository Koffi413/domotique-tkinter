from controllers import requete_utilisateurs as bd
from fonctions.fonctions_glob import etape, suivant

bullet = "\u2022"
def creer(suiv,nomUser,mdpUser):
    nom = nomUser.get()
    mdp = mdpUser.get()
    insert = bd.ajouterUtilisateurs(nom, mdp)
    if insert:
        suiv.place(x=1050, y=590)

def afficher_mdp(btn_oeil_mdp,champMdp,oeil_ouvert,oeil_ferme):
    if champMdp.cget("show") == bullet:
       btn_oeil_mdp.configure(image=oeil_ouvert)
       champMdp.configure(show="")
    else:
       btn_oeil_mdp.configure(image=oeil_ferme)
       champMdp.configure(show=bullet)
def afficher_conf(btn_oeil_conf,champConf,oeil_ouvert,oeil_ferme):
    if champConf.cget("show") == bullet:
       btn_oeil_conf.configure(image=oeil_ouvert)
       champConf.configure(show="")
    else:
        champConf.configure(show=bullet)
        btn_oeil_conf.configure(image=oeil_ferme)

def etats(root,creation,btn_oeil_mdp,champMdp,btn_oeil_conf,mess,barreCompte,etapeCompte,etapeFin,etapeConf,barreFin,barreConf,champConf,nomUser,mdpUser,confMdp):
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
          root.after(3000, mess.place_forget)
       else:
          mess.configure(text="Les deux mots de passe sont différents", text_color="#ffc107")
          mess.cget("font").configure(size=12)
          mess.place(x=280, y=310)
    else:
       creation.configure(state="disabled")
       creation.configure(fg_color="#D9D9D9")
    if etape == 0:
       barreCompte.configure(fg_color="#212529")
       etapeCompte.configure(text_color="#212529")
       barreConf.configure(fg_color="#D9D9D9")
       etapeConf.configure(text_color="#D9D9D9")
       barreConf.configure(fg_color="#D9D9D9")
       barreFin.configure(fg_color="#D9D9D9")
       etapeFin.configure(text_color="#D9D9D9")
