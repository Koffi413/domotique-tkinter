import customtkinter

from controllers.requete_maisons import ajouterMaisons, existeMaison
from controllers.requete_pieces import ajouterPieces,listePieces
from fonctions.fonctions_creation_compte import bullet


def activeValide(root,btnvalid,nomMaison,nomPiece,typePiece,superficiePiece,btnAjout,champMais,champPiece,btnsuiv,frameConfig):
       nomMais = nomMaison.get()
       nomPie = nomPiece.get()
       superficiePie = superficiePiece.get()
       typePie = typePiece.get()
       btnAjout.configure(state="disabled")
       if (nomMais!="" and nomPie!="" and superficiePie!="0" and typePie!=0) or (nomMais!="" and nomPie!="" and superficiePie=="" and typePie==0):
           btnvalid.configure(state="normal")
           btnvalid.configure(fg_color="#0d6efd")
           btnvalid.configure(hover_color="#3f8cfd")
           btnvalid.configure(command=lambda :save(root,btnvalid,nomMaison,nomPiece,typePiece,superficiePiece,btnAjout,champMais,champPiece,btnsuiv,frameConfig))
       else:
              btnvalid.configure(state="disabled")


def save(root,btnvalid,nomMaison,nomPiece,typePiece,superficiePiece,btnAjout,champMais,champPiece,btnsuiv,frameConfig):
    nomMais=nomMaison.get()
    nomPiec = nomPiece.get()
    superficiePie=superficiePiece.get()
    typePie=typePiece.get()
    if typePie==1:
        type="salon"
    elif typePie==2:
        type="chambre"
    elif typePie==3:
        type="cuisine"
    elif typePie==4:
        type="salle de bain"
    else:
        type="undefined"
    existe = existeMaison(nomMais)

    if len(existe)==0 :
        insertMaison = ajouterMaisons(nomMais,0)
        if insertMaison:
            champMais.configure(state="disabled")
            champMais.configure(fg_color="#e6e6e6")
            insert = ajouterPieces(nomPiec,superficiePie,18,0,nomMais,type)
            if insert:
                resumeAjout(nomMais,frameConfig)
                btnvalid.configure(state="disabled")
                btnvalid.configure(fg_color="#D9D9D9")
                btnvalid.configure(hover_color="#D9D9D9")
                btnAjout.configure(state="normal")
                btnAjout.configure(fg_color="#0d6efd")
                btnAjout.configure(hover_color="#3f8cfd")
                btnAjout.configure(command=lambda :renitialise(root,nomPiece,typePiece,superficiePiece,btnAjout,champPiece,btnsuiv))
                btnsuiv.place(relx=0.95, rely=0.90, anchor="se")
    else:
        champMais.configure(state="disabled")
        champMais.configure(fg_color="#e6e6e6")
        insert = ajouterPieces(nomPiec, superficiePie, 18, 0, nomMais, type)
        if insert:
            resumeAjout(nomMais,frameConfig)
            btnvalid.configure(state="disabled")
            btnvalid.configure(fg_color="#D9D9D9")
            btnvalid.configure(hover_color="#D9D9D9")
            btnAjout.configure(state="normal")
            btnAjout.configure(fg_color="#0d6efd")
            btnAjout.configure(hover_color="#3f8cfd")
            btnAjout.configure(command=lambda: renitialise(root, nomPiece, typePiece, superficiePiece, btnAjout, champPiece,btnsuiv))
            btnsuiv.place(relx=0.95, rely=0.90, anchor="se")

def renitialise(root,nomPiece,typePiece,superficiePiece,btnAjout,champPiece,btnsuiv):
    btnsuiv.place_forget()
    root.update()
    champPiece.focus_set()
    nomPiece.set("")
    superficiePiece.set(0)
    typePiece.set(0)
    btnAjout.configure(state="disabled")
    btnAjout.configure(fg_color="#D9D9D9")
    btnAjout.configure(hover_color="#D9D9D9")

def resumeAjout(nomMaison,frameConfig):
    liste=[]
    liste = listePieces(nomMaison)
    if len(liste)==0:
        return
    else:
        Labposx=20
        posy=420
        bulposx = 0
        for x in liste:
            if posy == 600:
                Labposx =Labposx+400
                posy=420
                bulposx = bulposx+400
            bul = customtkinter.CTkLabel(frameConfig,text=bullet)
            bul.place(x=bulposx,y=posy)
            label = customtkinter.StringVar()
            label.set(f"{x[0]} , {x[2]} de {x[1]} m²")
            element = customtkinter.CTkLabel(frameConfig,textvariable=label)
            element.place(x=Labposx, y=posy)
            posy=posy+30




