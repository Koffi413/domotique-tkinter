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
    frameRec.pack(expand=True)
    titre = customtkinter.CTkLabel(frameRec,text=f"Maison:{maison}")
    titre.cget("font").configure(size=40)
    titre.place(x=240, y=0)
    logoValide =  customtkinter.CTkImage(light_image=Image.open("icons/verifie.png"), size=(20,20))
    imgValide = customtkinter.CTkLabel(frameRec,text="", image=logoValide)
    recap(maison,frameRec,imgValide)
    bouton.configure(text="Terminé")
    bouton.configure(fg_color="#198754")
    bouton.configure(hover_color="#21b26f")
    bouton.configure(command=lambda :redemarrer())
    bouton.place(x=1050, y=590)
