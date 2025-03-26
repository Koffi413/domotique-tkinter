from modeles import utilisateurs as compte
from database import connect as connection

def ajouterUtilisateurs(nom,mdp):
    try:
        individu = compte.Utilisateur(nom.get(), mdp.get())
        requete ="INSERT INTO UTILISATEURS(nom,mot_de_passe) values(?,?)"
        connection.cursor.execute(requete,(individu.nom,individu.mot_de_passe))
        connection.connect.commit()
        return True
    except connection.connect.Error as e:
        return False
    finally:
        connection.cursor.close()
        connection.connect.close()
