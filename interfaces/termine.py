import customtkinter
from  PIL import Image

from fonctions.fonctions_glob import redemarrer
from fonctions.fonctions_recap import recap


def afficherPageRecap(root, bouton, maison):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.title('KeepControl')
    frameRec = customtkinter.CTkFrame(root, width=800, height=400)
    frameRec.place(relx=0.5, rely=0.5, anchor="center")
    titre = customtkinter.CTkLabel(frameRec,text=f"Maison: {maison}")
    titre.cget("font").configure(size=40)
    titre.place(x=240, y=0)
    recap(maison,frameRec)
    bouton.configure(text="Terminé")
    bouton.configure(fg_color="#198754")
    bouton.configure(hover_color="#21b26f")
    bouton.configure(command=lambda :redemarrer())
    bouton.place(relx=0.95, rely=0.90, anchor="se")
    texte = ("Lorsque vous cliquez sur 'Terminé', l'application va redémarrer automatiquement.\n"
             "À la relance, vous devrez vous reconnecter avec vos identifiants.\n"
             "Assurez-vous d'avoir vos informations de connexion à disposition.")
    label = customtkinter.CTkLabel(frameRec, text=texte, font=("Lota Grotesque", 18), wraplength=750, justify="center")
    label.place(relx=0.5, rely=0.95, anchor="s")
