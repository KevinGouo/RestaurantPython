from Restau.Personne import *
from Restau.Restaurant import *
from Restau.Avis import *
from datetime import date

bdd = Bdd_Avis()
bdd_Resto = Bdd_Resto()
bdd_users = Bdd_Personne()


def Avis_Client():
    date1 = date(2018, 12, 5)
    date2 = date(2017, 8, 28)
    date3 = date(2019, 5, 14)

    A1 = Avis("Nakata", "Dupont", str(date1), str(8), "Service de grande qualité")
    bdd.add(A1)
    A2 = Avis("L'abeille", "Azerty", str(date2), str(9),
              "Un repas d'excellent qualité, une bonne ambiance malgré un prix assez excessive, l'abeille reste un must de la gastronomie française ")
    bdd.add(A2)
    A3 = Avis("Mc'Donalds", "BigMic", str(date3), str(3),
              "Publicité mensongères, des burgers différents de ceux vus affichés et l'état des lieux laissaient a désirer")
    bdd.add(A3)


def Liste_Avis():
    print(bdd)


def Publication():
    nom = input("Quel est le nom du restaurant que vous voulez juger ")
    auteur = input("Quel est votre nom? ")
    jour = date.today()

    try:
        note = int(input("Quel note sur 5? "))
    except ValueError:
        print("Rentrez un chiffre!!!")
        note = int(input("Quel note sur 5? "))

    while note < 0 or note > 5:
        print("Veuillez indiquer un chiffre entre 0 et 5 svp")
        note = int(input("Quel note sur 5? "))

    comm = input("Quel est votre commentaire sur ce retaurant? ")
    Ax = Avis(nom, auteur, str(jour), str(note), comm)
    bdd.add(Ax)


def Restaurant():
    F1 = FastFood(str(151), "Mc'Donalds", "Burgers", str(15), "17 rue Jean Jaurès", str(10), str(0), "oui")
    bdd_Resto.add(F1)
    F2 = FastFood(str(41), "Pizza Hut", "Pizzas", str(4), "2 rue Lakanal", str(7), str(0), "oui")
    bdd_Resto.add(F2)
    F3 = FastFood(str(131), "Nakata", "Sushis", str(13), "2 rue du Nouveau Ming", str(15), str(0), "oui")
    bdd_Resto.add(F3)
    RT1 = RestoTraditionnel(str(1011), "Chez Renault", "Belge", str(1), "69 boulevard Haussmann", str(80), str(3),
                            "non", "oui")
    bdd_Resto.add(RT1)
    RT2 = RestoTraditionnel(str(1811), "Chez Gino", "Italienne", str(8), "7 avenue Montaigne", str(50), str(2), "oui",
                            "non")
    bdd_Resto.add(RT2)
    RT3 = RestoTraditionnel(str(1711), "Kongossa", "Africaine", str(18), "20 allée de la Reine", str(30), str(2), "oui",
                            "non")
    bdd_Resto.add(RT3)
    RL1 = RestoLuxe(str(3821), "Fouquet's", "Francaise", str(8), "99 Avenue des Champs-Elysées", str(100), str(4),
                    "non", "oui", str(7))
    bdd_Resto.add(RL1)
    RL2 = RestoLuxe(str(3621), "L'abeille", "Francaise", str(16), " 10 Avenue d'Iéna", str(100), str(5), "non", "non",
                    str(10))
    bdd_Resto.add(RL2)


def Liste_Resto():
    print(bdd_Resto)


def Ajout_Resto():
    try:
        id = int(input("Quel est l'identifiant du restaurant que vous voulez ajouter ?"))
    except ValueError:
        print("Rentrez un chiffre!!!")
        id = int(input("Quel est l'identifiant du restaurant que vous voulez ajouter ?"))

    nom = input("Quel est le nom du restaurant que vous voulez ajouter? ")
    cuisine = input("Quel est le type de cuisine? ")

    try:
        prix = float(input("Quel est le prix moyen ? "))
    except ValueError:
        print("Rentrez un chiffre!!!")
        prix = float(input("Quel est le prix moyen ? "))

    try:
        arrondissement = int(input("Dans quel arrondissement de Paris? "))
    except ValueError:
        print("Rentrez un chiffre!!!")
        arrondissement = int(input("Dans quel arrondissement de Paris? "))

    while arrondissement < 1 or arrondissement > 20:
        print("Veuillez indiquer un chiffre entre 0 et 20 svp")
        arrondissement = int(input("Dans quel arrondissement de Paris? "))

    adresse = input("Quel est l'adresse ? ")

    try:
        etoile = int(input("Combien d'étoiles sur 5? "))
    except ValueError:
        print("Rentrez un chiffre!!!")
        etoile = int(input("Combien d'étoiles sur 5? "))

    while etoile < 0 or etoile > 5:
        print("Veuillez indiquer un chiffre entre 0 et 5 svp")
        etoile = int(input("Combien d'étoiles sur 5? "))

    if id < 1000:
        print("\nAJOUT DE FAST FOOD\n")
        ppe = input("A emporter? ")
        Fx = FastFood(str(id), nom, cuisine, str(prix), str(arrondissement), adresse, str(etoile), ppe)
        bdd_Resto.add(Fx)
    elif 1000 < id < 3000:
        print("\nAJOUT DE RESTAURATION TRADITIONNEL\n")
        am = input("Ambiance Musicale")
        ah = input("Ambiance Musicale")
        RTx = RestoTraditionnel(str(id), nom, cuisine, str(prix), str(arrondissement), adresse, str(etoile), am, ah)
        bdd_Resto.add(RTx)
    elif id > 3000:
        print("\nAJOUT DE RESTAURATION LUXE\n")
        am = input("Ambiance Musicale ")
        ah = input("Acccès handicapés ")
        try:
            recompense = input("Indiquez le nombre de récompenses obtenu ")
        except ValueError:
            print("Rentrez un chiffre!!!")
            recompense = input("Indiquez le nombre de récompenses obtenu ")
        RLx = RestoLuxe(str(id), nom, cuisine, str(prix), str(arrondissement), adresse, str(etoile), am, ah,
                        str(recompense))
        bdd_Resto.add(RLx)


def Clear_Resto():
    bdd_Resto.bddr.clear()


def Statut():
    U1 = User(str(1), "cpo@epfedu.fr", "TacTic", "algo")
    bdd_users.add(U1)
    UP1 = UserPremium(str(2), "theop@epfedu.fr", "zxoe", "hydro")
    bdd_users.add(UP1)
    A1 = Admin(str(0), "kgm@epfedu.fr", "Zidane", "z")
    bdd_users.add(A1)


def Liste_statut():
    print(bdd_users)


def New_User():
    try:
        role = int(input("Utilisateur simple (1) ou premium (2) ? "))
    except ValueError:
        print("Rentrez un chiffre!!!")
        role = int(input("Utilisateur simple (1) ou premium (2) ? "))

    while role < 1 or role > 2:
        print("Veuillez choisir entre 1 et 2 svp")
        role = int(input("Utilisateur simple (1) ou premium (2) ?"))

    mail = input("Quel est votre mail ? ")
    pseudo = input("Quel est votre pseudo ? ")
    mdp = input("Quel est votre mdp ? ")

    if str(role) == str(1):
        print("\nUTILISATEUR SIMPLE\n")
        Ux = User(str(1), mail, pseudo, mdp)
        bdd_users.add(Ux)
    else:
        print("\nUTILISATEUR PREMIUM\n")
        UPx = User(str(2), mail, pseudo, mdp)
        bdd_users.add(UPx)


def test():
    fichier = open("test.txt", "a")
    fichier.write(str(bdd_Resto))
    fichier.close()


def ViderFR():
    fichier = open("test.txt", "w")
    fichier.write("-")


def RechercheR():
    with open("test.txt", "r") as f:
        for line in f.readlines():
            if "Nom:" in line:
                print(line)
            if "Identifiant" in line:
                print(line)
            if "Prix" in line:
                print(line + "\n")


def testA():
    fichier = open("avis.txt", "a")
    fichier.write(str(bdd))
    fichier.close()


def ViderFA():
    fichier = open("avis.txt", "w")
    fichier.write("-")


def testU():
    fichier = open("user.txt", "a")
    fichier.write(str(bdd_users))
    fichier.close()


def ViderFU():
    fichier = open("user.txt", "w")
    fichier.write("-")
