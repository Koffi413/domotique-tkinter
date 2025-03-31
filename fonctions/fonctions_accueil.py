import customtkinter
from  PIL import Image

from controllers.requete_maisons import trouverMaison
from controllers.requete_pieces import listePieces, listeTypePiece

iconReglage = customtkinter.CTkImage(light_image=Image.open("icons/reglage.png"), size=(20,20))
iconUser= customtkinter.CTkImage(light_image=Image.open("icons/user.png"), size=(20,20))

def page(nom,titre):
    maisonUser = trouverMaison(nom)
    titre.configure(text=maisonUser[0][0].upper())
    titre.place(relx=0.5,rely=0.1, anchor='center')
def typePieces(nomMaison,type):
    piece = listeTypePiece(nomMaison,type)
    #if len(piece) > 0:
        #for i in range(len(piece)):
