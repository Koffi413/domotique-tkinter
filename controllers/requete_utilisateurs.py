import sqlite3

from modeles import utilisateurs as compte
from database import connect as connection

def ajouterUtilisateurs(nom,mdp):
    try:
        individu = compte.Utilisateur(nom, mdp)
        requete ="""INSERT INTO UTILISATEURS(nom,mot_de_passe) values(?,?)"""
        connection.curseur.execute(requete,(individu.nom,individu.mot_de_passe))
        connection.connect.commit()
        return True
    except sqlite3.Error as e:
        return False
