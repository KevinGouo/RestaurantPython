class Perso:

    def __init__(self, role: int, email: str, pseudo: str, mdp: str):
        self.email = email
        self.pseudo = pseudo
        self.mdp = mdp
        self.role = role

    def __str__(self):
        return "Email: {} \nPseudo: {}\nMot de passe: {}\n".format(self.email, self.pseudo, self.mdp, self.role)

    def get_pseudo(self):
        return self.pseudo

    def get_email(self):
        return self.email

    def get_mdp(self):
        return self.mdp

    def get_role(self):
        return self.role


class Admin(Perso):

    def __init__(self, role: int, email: str, pseudo: str, mdp: str):
        self.email = email
        self.pseudo = pseudo
        self.mdp = mdp
        self.role = role

    def __str__(self):
        return "Email: {} \nPseudo: {}\nMot de passe: {}\n".format(self.email, self.pseudo, self.mdp, self.role)


class User(Perso):

    def __init__(self, role: int, email: str, pseudo: str, mdp: str):
        self.email = email
        self.pseudo = pseudo
        self.mdp = mdp
        self.role = role

    def __str__(self):
        return "Email: {} \nPseudo: {}\nMot de passe: {}\n".format(self.email, self.pseudo, self.mdp, self.role)


class UserPremium(User):

    def __init__(self, role: int, email: str, pseudo: str, mdp: str):
        self.email = email
        self.pseudo = pseudo
        self.mdp = mdp
        self.role = role

    def __str__(self):
        return "Email: {} \nPseudo: {}\nMot de passe: {}\n".format(self.email, self.pseudo, self.mdp, self.role)


class Bdd_Personne:

    def __init__(self):
        self.bddp = dict()

    def __str__(self):
        string = "Utilisateur:\n"
        for entry in self.bddp:
            string += str(entry)
            string += "\n"
        return string

    def add(self, perso: Perso):
        self.bddp[perso] = perso
