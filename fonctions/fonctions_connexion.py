bullet = "\u2022"
def afficher_mdp(btn_oeil_mdp,champMdp,oeil_ouvert,oeil_ferme):
    if champMdp.cget("show") == bullet:
       btn_oeil_mdp.configure(image=oeil_ouvert)
       champMdp.configure(show="")
    else:
       champMdp.configure(show=bullet)
       btn_oeil_mdp.configure(image=oeil_ferme)
def connect(app,nomUser,mdpUser):
    nom = nomUser.get()
    mdp = mdpUser.get()
def etat(connexion,btn_oeil_mdp,champMdp,nomUser,mdpUser):
    nom = nomUser.get()
    mdp = mdpUser.get()
    if len(mdp) > 0:
        btn_oeil_mdp.place(in_=champMdp, relx=1, rely=0.5, anchor="e")

    if nom != "" and mdp != "":
        connexion.configure(state="normal")
        connexion.configure(fg_color="#0d6efd")
        connexion.configure(hover_color="#3f8cfd")
    else:
       connexion.configure(state="disabled")
