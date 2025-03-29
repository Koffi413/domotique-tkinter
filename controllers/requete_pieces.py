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
def listePieces(nomMaison):
    try:
        piece = Piece(None,None,nomMaison,None,None,None)
        req= """SELECT *  FROM PIECES WHERE nomMaison=?"""
        connection.curseur.execute(req,(piece.nomMaison,))
        listp = connection.curseur.fetchall()
        return listp
    except connection.connect.Error as e:
        return []