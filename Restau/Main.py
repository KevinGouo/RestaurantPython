from Restau.Conseiller import *

Restaurant()
Avis_Client()
Statut()

choix = 0
while choix != 11:

    try:
        choix = int(input("1) Afficher la liste de tous les restaurants\n"
                          "2) Ajouter un restaurant à la liste\n"
                          "3) Afficher la liste de tous les avis\n"
                          "4) Ajouter un avis \n"
                          "5) Afficher la liste d'utilisateurs\n"
                          "6) Créer un compte\n"
                          "7) Sauvegarder dans un fichier les restaurants\n"
                          "8) Afficher les restaurants avec leur prix\n"
                          "9) Sauvegarder dans un fichier les avis\n"
                          "10) Sauvegarder dans un fichier les utilisateurs\n"
                          "11) Quitter\n"))
    except ValueError:
        print("Rentrez un chiffre!!!")
        choix

    if choix < 1 or choix > 11:
        print("Veuillez indiquer un chiffre entre 1 et 11 svp")
        choix

    if choix == 1:
        Liste_Resto()
    elif choix == 2:
        Ajout_Resto()
        Liste_Resto()
    elif choix == 3:
        Liste_Avis()
    elif choix == 4:
        Publication()
        Liste_Avis()
    elif choix == 5:
        Liste_statut()
    elif choix == 6:
        New_User()
        Liste_statut()
    elif choix == 7:
        ViderFR()
        test()
        print("Sauvegarde effectué !!\n")
    elif choix == 8:
        RechercheR()
    elif choix == 9:
        ViderFA()
        testA()
        print("Sauvegarde effectué !!\n")
    elif choix == 10:
        ViderFU()
        testU()
        print("Sauvegarde effectué !!\n")
    elif choix == 11:
        exit()