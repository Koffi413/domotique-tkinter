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
        nombrePiece integer,
        user text not null ,
        foreign key (user) references UTILISATEURS (Nom)
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
    curseur.execute("INSERT OR IGNORE INTO UTILISATEURS (Nom, mot_de_passe) VALUES (?, ?)", ("jean", "mdp"))

    # Insérer une maison associée à cet utilisateur
    curseur.execute("INSERT OR IGNORE INTO MAISONS (Nom, nombrePiece, user) VALUES (?, ?, ?)",
                    ("maisonjean", 0, "jean"))

    # Insérer 24 pièces (6 salons, 6 chambres, 6 cuisines, 6 salles de bain)
    pieces = [
        ("salon1", 25, "Salon", "maisonjean", 22, 1),
        ("salon2", 28, "Salon", "maisonjean", 22, 1),
        ("salon3", 30, "Salon", "maisonjean", 21, 1),
        ("salon4", 27, "Salon", "maisonjean", 22, 1),
        ("salon5", 26, "Salon", "maisonjean", 22, 1),
        ("salon6", 29, "Salon", "maisonjean", 21, 1),

        ("chambre1", 15, "Chambre", "maisonjean", 20, 1),
        ("chambre2", 12, "Chambre", "maisonjean", 18, 1),
        ("chambre3", 14, "Chambre", "maisonjean", 19, 1),
        ("chambre4", 16, "Chambre", "maisonjean", 20, 1),
        ("chambre5", 13, "Chambre", "maisonjean", 19, 1),
        ("chambre6", 17, "Chambre", "maisonjean", 18, 1),

        ("cuisine1", 18, "Cuisine", "maisonjean", 21, 1),
        ("cuisine2", 20, "Cuisine", "maisonjean", 21, 1),
        ("cuisine3", 22, "Cuisine", "maisonjean", 21, 1),
        ("cuisine4", 19, "Cuisine", "maisonjean", 21, 1),
        ("cuisine5", 21, "Cuisine", "maisonjean", 21, 1),
        ("cuisine6", 23, "Cuisine", "maisonjean", 21, 1),

        ("salledebain1", 10, "Salle de Bain", "maisonjean", 24, 1),
        ("salledebain2", 8, "Salle de Bain", "maisonjean", 23, 1),
        ("salledebain3", 9, "Salle de Bain", "maisonjean", 24, 1),
        ("salledebain4", 11, "Salle de Bain", "maisonjean", 24, 1),
        ("salledebain5", 7, "Salle de Bain", "maisonjean", 23, 1),
        ("salledebain6", 12, "Salle de Bain", "maisonjean", 24, 1),
    ]

    # Exécution des requêtes d'insertion
    curseur.executemany(
        "INSERT INTO PIECES (Nom, superficie, type, nomMaison, temperature, ampoule) VALUES (?, ?, ?, ?, ?, ?)", pieces)

    # Valider les changements
    connect.commit()