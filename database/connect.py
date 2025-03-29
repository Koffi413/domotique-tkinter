import sqlite3, os.path
bd = os.path.exists("database/projetIsiDatabase.db")
connect = sqlite3.connect("database/projetIsiDatabase.db")
curseur = connect.cursor()
if not bd:
    curseur.execute(
        """
        create table UTILISATEURS (
        Nom text not null primary key ,
        mot_de_passe text not null
        );
        """
    )
    connect.commit()
    curseur.execute(
        """
        create table MAISONS (
        Nom text not null primary key ,
        nombrePiece integer 
        );"""
    )
    connect.commit()
    curseur.execute(
        """
        create table PIECES (
        Nom text not null,
        superficie integer not null,
        type text not null,
        nomMaison text not null,
        temperature integer not null,
        ampoule integer not null,
        foreign key (nomMaison) references MAISONS (Nom)
        );
        """
    )
    connect.commit()
    curseur.execute(
        """
        CREATE TRIGGER UpdateNombrePieces_AfterInsert
        AFTER INSERT ON PIECES
        FOR EACH ROW
        BEGIN
            UPDATE MAISONS
             SET nombrePiece = (SELECT COUNT(*) FROM PIECES WHERE nomMaison = NEW.nomMaison)
             WHERE Nom = NEW.nomMaison;
        END;
        """
    )
    connect.commit()