import customtkinter
from  PIL import Image

from interfaces.creation_compte import afficherPageCompte
from interfaces.configurationMaison import afficherPageConfig

if __name__ == '__main__':
    customtkinter.set_default_color_theme("theme/theme.json")
    logo = customtkinter.CTkImage(light_image=Image.open("icons/logo.png"), size=(150, 150))
    root = customtkinter.CTk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.title('KeepControl')
    im = customtkinter.CTkLabel(root, text="", image=logo)
    im.place(x=0, y=0)
    suiv = customtkinter.CTkButton(root, text="Suivant", text_color="white", width=200, height=40)
    suiv.place_forget()

    # Progression
    framePro = customtkinter.CTkFrame(root, width=1250, height=58, fg_color="white")
    framePro.pack(side="bottom")
    # etape
    barreCompte = customtkinter.CTkFrame(framePro, width=450, height=10, corner_radius=0,fg_color="#212529")
    barreCompte.place(x=0, y=0)
    etapeCompte = customtkinter.CTkLabel(framePro, text="Création de compte",text_color="#212529" )
    etapeCompte.cget("font").configure(size=25)
    etapeCompte.place(x=100, y=15)
    barreConf = customtkinter.CTkFrame(framePro, width=450, height=10, corner_radius=0,fg_color="#D9D9D9")
    barreConf.place(x=450, y=0)
    etapeConf = customtkinter.CTkLabel(framePro, text="Configuration de la maison",text_color="#D9D9D9" )
    etapeConf.cget("font").configure(size=25)
    etapeConf.place(x=520, y=15)
    barreFin = customtkinter.CTkFrame(framePro, width=450, height=10, corner_radius=0,fg_color="#D9D9D9")
    barreFin.place(x=900, y=0)
    etapeFin = customtkinter.CTkLabel(framePro, text="Terminé",text_color="#D9D9D9")
    etapeFin.cget("font").configure(size=25)
    etapeFin.place(x=1050, y=15)
    afficherPageCompte(root,suiv)
    root.mainloop()