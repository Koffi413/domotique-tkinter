import  customtkinter
from PIL import Image,ImageTk
customtkinter.set_default_color_theme("../theme/theme.json")
etape=0
oeil_ouvert = customtkinter.CTkImage(light_image=Image.open("../icons/ouvert.png"), size=(20,20))
oeil_ferme= customtkinter.CTkImage(light_image=Image.open("../icons/fermé.png"),size=(20,20))
def afficher_mdp():
    if champMdp.cget("show") == bullet:
        btn_oeil_mdp.configure(image=oeil_ouvert)
        champMdp.configure(show="")
    else:
        btn_oeil_mdp.configure(image=oeil_ferme)
        champMdp.configure(show=bullet)
def afficher_conf():
    if champConf.cget("show") == bullet:
        btn_oeil_conf.configure(image=oeil_ouvert)
        champConf.configure(show="")
    else:
        champConf.configure(show=bullet)
        btn_oeil_conf.configure(image=oeil_ferme)

def etats():
    nom = nomUser.get()
    mdp = mdpUser.get()
    conf = confMdp.get()
    if len(mdp)>0:
        btn_oeil_mdp.place(in_=champMdp, relx=1, rely=0.5, anchor="e")
    if len(conf) > 0:
        btn_oeil_conf.place(in_=champConf, relx=1, rely=0.5,anchor="e")

    if nom != "" and mdp != "" and conf != "":
        if mdp == conf:
            mess.place_forget()
            creation.configure(state="normal")
            creation.configure(fg_color="#0d6efd")
            app.after(3000, mess.place_forget)
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
app = customtkinter.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.title('KeepControl')
#formulaire de connexion
nomUser = customtkinter.StringVar()
mdpUser = customtkinter.StringVar()
confMdp = customtkinter.StringVar()
frameForm = customtkinter.CTkFrame(app, width=800, height=350)
frameForm.pack(expand=True)
formTitre = customtkinter.CTkLabel(frameForm,text="Compte Personnel", font=("Lota Grotesque", 40))
formTitre.place(x=20, y=20)
formNom = customtkinter.CTkLabel(frameForm,text="Nom utilisateur :",)
formNom.place(x=20, y=120)
champNom = customtkinter.CTkEntry(frameForm, textvariable=nomUser,width=350, height=30)
app.update()
champNom.focus_set()
champNom.cget("font").configure(size=17)
champNom.place(x=180,y=120)
formMdp = customtkinter.CTkLabel(frameForm,text="Mot de passe :")
formMdp.place(x=20, y=200)
bullet = "\u2022"
champMdp = customtkinter.CTkEntry(frameForm, textvariable=mdpUser,width=350, height=30,show=bullet)
champMdp.place(x=180,y=200)
btn_oeil_mdp = customtkinter.CTkButton(frameForm,text="",image=oeil_ferme, command=afficher_mdp,width=10)
btn_oeil_mdp.configure(fg_color="white")
btn_oeil_mdp.configure(hover_color="white")
btn_oeil_mdp.place_forget()
formConf = customtkinter.CTkLabel(frameForm,text="Confirmez mot de passe :")
formConf.place(x=20, y=280)
champConf = customtkinter.CTkEntry(frameForm, textvariable=confMdp,width=350, height=30, show=bullet)
champConf.place(x=280,y=280)
btn_oeil_conf = customtkinter.CTkButton(frameForm,text="",image=oeil_ferme, command=afficher_conf,width=10)
btn_oeil_conf.configure(fg_color="white")
btn_oeil_conf.configure(hover_color="white")
btn_oeil_conf.place_forget()
# Label message (caché au début)
mess = customtkinter.CTkLabel(frameForm, text="", text_color="#ffc107")
mess.place_forget()
#boutoncréation
creation = customtkinter.CTkButton(app, text="Créer compte", text_color="white", width=400, height=40)
creation.place(x=450,y=500)
#boutonsuivant
suiv = customtkinter.CTkButton(app, text="Suivant", text_color="white", width=200, height=40,fg_color="#6c757d")
suiv.place(x=1050,y=590)
#Progression
framePro = customtkinter.CTkFrame(app, width=1250, height=58, fg_color="white")
framePro.pack(side="bottom")
#etape
barreCompte = customtkinter.CTkFrame(framePro, width=450, height=10,corner_radius=0)
barreCompte.place(x=0,y=0)
etapeCompte=customtkinter.CTkLabel(framePro, text="Création de compte",)
etapeCompte.cget("font").configure(size=25)
etapeCompte.place(x=100, y=15)
barreConf = customtkinter.CTkFrame(framePro, width=450, height=10,corner_radius=0)
barreConf.place(x=450,y=0)
etapeConf=customtkinter.CTkLabel(framePro, text="Configuration de la maison",)
etapeConf.cget("font").configure(size=25)
etapeConf.place(x=520, y=15)
barreFin = customtkinter.CTkFrame(framePro, width=450, height=10,corner_radius=0)
barreFin.place(x=900,y=0)
etapeFin=customtkinter.CTkLabel(framePro, text="Terminé")
etapeFin.cget("font").configure(size=25)
etapeFin.place(x=1050, y=15)
etats()
nomUser.trace("w", lambda *args: etats())
mdpUser.trace("w", lambda *args: etats())
confMdp.trace("w", lambda *args: etats())
app.mainloop()
