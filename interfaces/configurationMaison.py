import customtkinter
from PIL import Image,ImageTk

def afficherPageConfig(app):

    def radiobutton_event():
        print("radiobutton toggled, current value:", radio_var.get())
#frame Config
    frameConfig = customtkinter.CTkFrame(app, width=1100, height=600)
    frameConfig.place(x=150, y=20)
    frameTitre = customtkinter.CTkLabel(frameConfig,text="Configurations")
    frameTitre.cget("font").configure(size=30)
    frameTitre.place(x=7,y=7)
    #formulaire ajout de pieces
    labMais = customtkinter.CTkLabel(frameConfig, text="Nommez vôtre maison:")
    labMais.place(x=15,y=100)
    champMais = customtkinter.CTkEntry(frameConfig, width=400, height=30, placeholder_text="Ex: maison de vacances")
    champMais.place(x=250, y=100)
    labPiece= customtkinter.CTkLabel(frameConfig, text="Nom de la pièce:")
    labPiece.place(x= 15, y=180)
    champPiece = customtkinter.CTkEntry(frameConfig, width=400,height=30, placeholder_text="Ex: chambre de Junior")
    champPiece.place(x=180, y=180)

    labType = customtkinter.CTkLabel(frameConfig, text="Type de pièce:")
    labType.place(x=15, y=260)
    radio_var = customtkinter.IntVar(value=0)
    salon = customtkinter.CTkRadioButton(frameConfig, text="Salon",command=radiobutton_event, variable= radio_var, value=1)
    salon.place(x=180,y=260)
    chambre = customtkinter.CTkRadioButton(frameConfig, text="Chambre",command=radiobutton_event, variable= radio_var, value=2)
    chambre.place(x=300,y=260)
    cuisine = customtkinter.CTkRadioButton(frameConfig, text="Cuisine",command=radiobutton_event, variable= radio_var, value=3)
    cuisine.place(x=460,y=260)
    salbain = customtkinter.CTkRadioButton(frameConfig, text="Salle de bain",command=radiobutton_event, variable= radio_var, value=4)
    salbain.place(x=580,y=260)
    labSuperficie = customtkinter.CTkLabel(frameConfig,text="Superficie (m²):")
    labSuperficie.place(x=15,y=340)
    champSuperficie = customtkinter.CTkEntry(frameConfig, width=60,justify="center")
    champSuperficie.place(x=180, y=340)
    btnValid = customtkinter.CTkButton(frameConfig,text="Valider", width=80,height=30,text_color="white", fg_color="#D9D9D9",hover_color="#D9D9D9")
    btnValid.place(x=300,y =380)
    btnAjout = customtkinter.CTkButton(frameConfig,text="Ajouter une autre pièce", width=100,height=30,text_color="white", fg_color="#D9D9D9", hover_color="#D9D9D9")
    btnAjout.place(x=450,y =380)