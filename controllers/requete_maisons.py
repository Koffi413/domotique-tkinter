import sqlite3

from database import connect as connection
from modeles.maison import Maison


def ajouterMaisons(nom,nombrePiece):
    try:
        maison = Maison(nom,nombrePiece)
        requete = """INSERT INTO MAISONS values(?,?)"""
        connection.curseur.execute(requete, (maison.nom,maison.nombrePiece))
        connection.connect.commit()
        return True
    except connection.connect.Error as e:
        return False
def existeMaison(nom):
    try:
        maison = Maison(nom,None)
        requete = "SELECT * FROM MAISONS WHERE Nom = ?"
        connection.curseur.execute(requete, (maison.nom,))
        listeMais = connection.curseur.fetchall()
        return listeMais
    except sqlite3.Error as e:
        print(e)
        return []