import sqlite3

from modeles import utilisateurs as compte
from database import connect as connection

def ajouterUtilisateurs(nom,mdp):
    try:
        individu = compte.Utilisateur(nom, mdp)
        requete ="""INSERT INTO UTILISATEURS(Nom,mot_de_passe) values(?,?)"""
        connection.curseur.execute(requete,(individu.nom,individu.mot_de_passe))
        connection.connect.commit()
        return True
    except sqlite3.Error as e:
        return False
def existeUtilisateurs():
    try:
        req = """SELECT *  FROM UTILISATEURS"""
        connection.curseur.execute(req)
        reponse=connection.curseur.fetchall()
        return reponse
    except sqlite3.Error as e:
        return []
def trouverUtilisateurs(nom,mdp):
    try:
        individu = compte.Utilisateur(nom,mdp)
        req = """SELECT *  FROM UTILISATEURS WHERE LOWER(Nom) = LOWER(?) and mot_de_passe= ?"""
        connection.curseur.execute(req,(individu.nom,individu.mot_de_passe))
        rep = connection.curseur.fetchall()
        return rep
    except sqlite3.Error as e:
        return []

