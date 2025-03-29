class Utilisateur:
    def __init__(self, nom, mot_de_passe):
        self.nom = nom
        self.mot_de_passe=mot_de_passe
    def changerMdp(self, newMdp):
        self.mot_de_passe = newMdp
    def changerNom(self, newNom):
        self.nom=newNom
    def afficherInfos(self):
        return print(self.nom),print(self.mot_de_passe)