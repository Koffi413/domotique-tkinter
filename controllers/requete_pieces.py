from database import connect as connection
from modeles.pieces import Piece


def ajouterPieces(nom,superficie,temperature,ampoule,nomMaison,typePiece):
    try:
        piece = Piece(nom,typePiece,nomMaison,superficie,temperature,ampoule)
        requete ="""INSERT INTO PIECES values(?,?,?,?,?,?)"""
        connection.curseur.execute(requete,(piece.nom,piece.superficie,piece.type,piece.nomMaison,piece.temperature,piece.ampoule))
        connection.connect.commit()
        return True
    except connection.connect.Error as e:
        print(e)
        return False