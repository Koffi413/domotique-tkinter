import customtkinter

from controllers.requete_maisons import ajouterMaisons, existeMaison
from controllers.requete_pieces import ajouterPieces
from fonctions.fonctions_glob import suivant


def activeValide(root,btnvalid,nomMaison,nomPiece,typePiece,superficiePiece,btnAjout,champMais,champPiece,btnsuiv):
       nomMais = nomMaison.get()
       nomPie = nomPiece.get()
       superficiePie = superficiePiece.get()
       typePie = typePiece.get()
       btnAjout.configure(state="disabled")
       if (nomMais!="" and nomPie!="" and superficiePie!="0" and typePie!=0) or (nomMais!="" and nomPie!="" and superficiePie=="" and typePie==0):
           btnvalid.configure(state="normal")
           btnvalid.configure(fg_color="#0d6efd")
           btnvalid.configure(hover_color="#3f8cfd")
           btnvalid.configure(command=lambda :save(root,btnvalid,nomMaison,nomPiece,typePiece,superficiePiece,btnAjout,champMais,champPiece,btnsuiv))
       else:
              btnvalid.configure(state="disabled")


def save(root,btnvalid,nomMaison,nomPiece,typePiece,superficiePiece,btnAjout,champMais,champPiece,btnsuiv):
    nomMais=nomMaison.get()
    nomPiec=nomPiece.get()
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
                btnvalid.configure(state="disabled")
                btnvalid.configure(fg_color="#D9D9D9")
                btnvalid.configure(hover_color="#D9D9D9")
                btnAjout.configure(state="normal")
                btnAjout.configure(fg_color="#0d6efd")
                btnAjout.configure(hover_color="#3f8cfd")
                btnAjout.configure(command=lambda :renitialise(root,nomPiece,typePiece,superficiePiece,btnAjout,champPiece,btnsuiv))
                btnsuiv.place(x=1050, y=590)
    else:
        champMais.configure(state="disabled")
        champMais.configure(fg_color="#e6e6e6")
        insert = ajouterPieces(nomPiec, superficiePie, 18, 0, nomMais, type)
        if insert:
            btnvalid.configure(state="disabled")
            btnvalid.configure(fg_color="#D9D9D9")
            btnvalid.configure(hover_color="#D9D9D9")
            btnAjout.configure(state="normal")
            btnAjout.configure(fg_color="#0d6efd")
            btnAjout.configure(hover_color="#3f8cfd")
            btnAjout.configure(command=lambda: renitialise(root, nomPiece, typePiece, superficiePiece, btnAjout, champPiece,btnsuiv))
            btnsuiv.place(x=1050, y=590)

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


