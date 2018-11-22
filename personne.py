class Personne: # Nom de la classe

    # Constructeur de la classe. self est obligatoire mais ne compte pas comme argument
    def __init__(self, prenom, nom, age):
        # Toutes les variables self.quelquechose deviennent des variables membres de la classe
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.prenom_nom = self.prenom + " " + self.nom

    # Création d'une fonction de classe. 
    # Self ne compte pas, donc cette fonction n'a pas d'argument quand on l'appelle de l'extérieur.
    def se_presenter(self):
        print ("Salut, je m'appelle " + self.prenom_nom + " et j'ai " + str(self.age) + " ans.")
