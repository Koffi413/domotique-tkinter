import customtkinter

from controllers.requete_pieces import listePieces

def recap(nomMaison,frameRec,imgValide):
    pieces = listePieces(nomMaison)
    salon=[]
    chambre=[]
    cuisine =[]
    salBain=[]
    for piece in pieces:
        if piece[2]=="salon":
            salon.append(piece)
        elif piece[2]=="chambre":
            chambre.append(piece)
        elif piece[2]=="cuisine":
            cuisine.append(piece)
        else:
            salBain.append(piece)
    quantite=[{"type":"salon", "nbre":len(salon)}, {"type":"chambre", "nbre":len(chambre)}, {"type":"cuisine", "nbre":len(cuisine)}, {"type":"salle de bain", "nbre":len(salBain)}]
    posy=80
    for item in quantite:
        if item["nbre"]>0:
            imgValide.place(x=40, y=posy)
            element = customtkinter.CTkLabel(frameRec, text=f"{item["nbre"]} {item["type"]} ajouté")
            element.place(x=70, y=posy)
            posy=posy+40
