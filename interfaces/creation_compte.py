import  customtkinter
app = customtkinter.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.title('KeepControl')
#formulaire de connexion
frameForm = customtkinter.CTkFrame(app, width=900, height=350)
frameForm.pack(expand=True)
formTitre = customtkinter.CTkLabel(frameForm,text="Compte Personnel", font=("Roboto", 40))
formTitre.place(x=20, y=20)
formNom = customtkinter.CTkLabel(frameForm,text="Nom utilisateur :", font=("Roboto", 20))
formNom.place(x=20, y=120)
champNom = customtkinter.CTkEntry(frameForm, width=350, height=30)
champNom.place(x=180,y=120)
formMdp = customtkinter.CTkLabel(frameForm,text="Mot de passe :", font=("Roboto", 20))
formMdp.place(x=20, y=200)
champMdp = customtkinter.CTkEntry(frameForm, width=350, height=30)
champMdp.place(x=180,y=200)
formConf = customtkinter.CTkLabel(frameForm,text="Confirmez mot de passe :", font=("Roboto", 20))
formConf.place(x=20, y=280)
champConf = customtkinter.CTkEntry(frameForm, width=350, height=30)
champConf.place(x=280,y=280)
#boutonsuivant
suiv = customtkinter.CTkButton(app, text="Suivant", text_color="white", width=40, height=30, font=("Roboto", 18),fg_color="#0D6EFD")
suiv.place(x=1010,y=550)
#Progression
framePro = customtkinter.CTkFrame(app, width=1200, height=58)
framePro.pack(side="bottom")
#etape

app.mainloop()