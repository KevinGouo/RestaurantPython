
class Resto:

    def __init__(self, id: int, nom: str, cuisine: str, prix: float, arrondissement: int, adresse: str, etoile: int):
        self.nom = nom
        self.cuisine = cuisine
        self.id = id
        self.prix = prix
        self.arrondissement = arrondissement
        self.etoile = etoile
        self.adresse = adresse

    def __str__(self):
        return "Nom: {} \nType de cuisine: {}\nIdentifiant: {}\nPrix: {}€ \nArrondissement: {}\nNombre d'étoiles: {}`\n".format(self.nom, self.cuisine, self.id, self.prix, self.arrondissement, self.etoile)

    def get_nom(self):
        return self.nom

    def get_cuisine(self):
        return self.cuisine

    def get_id(self):
        return self.id

    def get_prix(self):
        return self.prix

    def get_arrondissement(self):
        return self.arrondissement

    def get_etoile(self):
        return self.etoile


class FastFood(Resto):

    def __init__(self, id: int, nom: str, cuisine: str, prix: float, arrondissement: int, adresse: str, etoile: int, ppe: str):
        self.nom = nom
        self.cuisine = cuisine
        self.id = id
        self.prix = prix
        self.arrondissement = arrondissement
        self.adresse = adresse
        self.etoile = etoile
        self.ppe = ppe

    def __str__(self):
        return "Nom: {} \nType de cuisine: {}\nIdentifiant: {}\nPrix: {}€ \nArrondissement: {}\nNombre d'étoiles: {}\nA " \
               "emporter: {}\n".format(self.nom, self.cuisine, self.id, self.prix, self.arrondissement, self.etoile, self.ppe)


class RestoTraditionnel(Resto):

    def __init__(self, id: int, nom: str, cuisine: str, prix: float, arrondissement: int, adresse: str, etoile: int, am: str, ah: str):
        self.nom = nom
        self.cuisine = cuisine
        self.id = id
        self.prix = prix
        self.arrondissement = arrondissement
        self.adresse = adresse
        self.etoile = etoile
        self.am = am
        self.ah = ah

    def __str__(self):
        return "Nom: {} \nType de cuisine: {}\nIdentifiant: {}\nPrix: {} \nArrondissement: {}\nNombre d'étoiles: {}" \
               "\nAmbiance Musicale: {}\nAccés handicapés: {}\n".format(self.nom, self.cuisine, self.id, self.prix, self.arrondissement, self.etoile, self.am, self.ah)


class RestoLuxe(RestoTraditionnel):

    def __init__(self, id: int, nom: str, cuisine: str, prix: float, arrondissement: int, adresse: str, etoile: int, am: str, ah: str, recompense: int):
        self.nom = nom
        self.cuisine = cuisine
        self.id = id
        self.prix = prix
        self.arrondissement = arrondissement
        self.adresse = adresse
        self.etoile = etoile
        self.am = am
        self.ah = ah
        self.recompense = recompense

    def __str__(self):
        return "Nom: {} \nType de cuisine: {}\nIdentifiant: {}\nPrix: {} \nArrondissement: {}\nNombre d'étoiles: {}\nAmbiance" \
               " Musicale: {}\nAccés handicapés: {}\nNombre de récompense: {}\n".format(self.nom, self.cuisine, self.id, self.prix, self.arrondissement, self.etoile, self.am, self.ah, self.recompense)


class Bdd_Resto:

    def __init__(self):
        self.bddr = dict()

    def __str__(self):
        string = "Restaurants:\n"
        for entry in self.bddr:
            string += str(entry)
            string += "\n"
        return string

    def add(self, resto: Resto):
        self.bddr[resto] = resto
