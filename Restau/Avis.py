from datetime import date

class Avis:

    def __init__(self, nom: str, auteur: str, date: date, note: int, comm: str):
        self.nom = nom
        self.auteur = auteur
        self.note = note
        self.date =date
        self.comm = comm

    def __str__(self):
        return "Nom du restaurant: " + self.nom + "\nAuteur du commentaire: " + self.auteur + "\nDate: " + self.date + "\nNote sur 5: " + self.note + "\nCommentaire: " + self.comm+ "\n"

    def get_nom(self):
        return self.nom

    def get_auteur(self):
        return self.auteur


class Bdd_Avis:

    def __init__(self):
        self.bdda = dict()

    def __str__(self):
        string = "Avis:\n"
        for entry in self.bdda:
            string += str(entry)
            string += "\n"
        return string

    def add(self, avis: Avis):
        self.bdda[avis] = avis