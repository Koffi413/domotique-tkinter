import sqlite3

from database import connect as connection
from modeles.maison import Maison


def ajouterMaisons(nom,nombrePiece,utilisateur):
    try:
        maison = Maison(nom,nombrePiece,utilisateur)
        requete = """INSERT INTO MAISONS values(?,?,?)"""
        connection.curseur.execute(requete, (maison.nom,maison.nombrePiece,maison.utilisateur))
        connection.connect.commit()
        return True
    except connection.connect.Error as e:
        return False
def existeMaison(nom):
    try:
        maison = Maison(nom,None,None)
        requete = "SELECT * FROM MAISONS WHERE Nom = ?"
        connection.curseur.execute(requete, (maison.nom,))
        listeMais = connection.curseur.fetchall()
        return listeMais
    except sqlite3.Error as e:
        print(e)
        return []
def trouverMaison(nom):
    try:
        maison = Maison(None,None,nom)
        requete = "SELECT * FROM MAISONS WHERE LOWER(user) = LOWER(?)"
        connection.curseur.execute(requete, (maison.utilisateur,))
        listeMais = connection.curseur.fetchall()
        return listeMais
    except sqlite3.Error as e:
        print(e)
        return []
