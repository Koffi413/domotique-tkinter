import sqlite3, os.path
bd = os.path.exists("../database/projetIsiDatabase.db")
connect = sqlite3.connect("../database/projetIsiDatabase.db")
cursor = connect.cursor()
if not bd:
    cursor.execute(
        """
        create table UTILISATEURS (
        id integer primary key autoincrement,
        Nom text not null,
        mot_de_passe text not null
        );
        """
    )
    connect.commit()