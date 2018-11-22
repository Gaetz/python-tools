# Fonction print avec un argument, qui affiche le texte passé en argumé
print("bonjour a tous")

# Ce texte est un commentaire. Il n'est pas lu par python.

# Création d'une variable numérique
nb_etudiants = 10
print(nb_etudiants)

# Création d'une variable booléenne (vrai ou faux)
booleen = True # or False
print(booleen)

# On augmente le chiffre dans la variable de 1
nb_etudiants = nb_etudiants + 1
print(nb_etudiants)

# Concaténation de deux chaines de caractères (string)
bonjour = "bonjour" + " a vous"
print(bonjour)

# On doit convertir le nombre en chaîne de caractère pour le concaténer
print(bonjour + " " + str(nb_etudiants))

# Définition et contenu d'une fonction
# Bien faire attention aux deux points après les parenthèses, et aux indentations (tabulations)
def accueil_nouvel_eleve():
    global nb_etudiants
    nb_etudiants = nb_etudiants + 1
    bonjour = "bonjour a vous " + str(nb_etudiants)
    print(bonjour)

# Appel de la fonction en utilisant les parenthèses
accueil_nouvel_eleve()

# On appelle 5 fois la fonction grace à la boucle for
for i in range(0, 5):
    accueil_nouvel_eleve()
    print(i)

# Création et affichage d'une liste
profs_jv = ["brice", "guillaume", "mathieu"]
for prenom in profs_jv:
    print(prenom)

# On récupère le deuxième élément de la liste (en programmation on commence à compter à 0)
guil = profs_jv[1]
print(guil)

# Affichage de la liste des profs à l'envers
for index in range(0, 2):
    print(profs_jv[2 - index])

# Création d'une fonction qui affiche à l'envers n'importe quelle liste
def lire_a_l_envers(liste):
    for index in range(0, len(liste)):
        print(liste[len(liste) - 1 - index])

print("-------")
lire_a_l_envers(profs_jv)

# Définition d'une fonction qui affiche un texte en fonction du nombre d'éléments d'une liste
def greetings(liste):
    if len(liste) < 4: # SI
        for name in liste:
            print("bonjour " + name)
    elif len(liste) == 4: # Sinon SI
        print("bonjour a vous quatre")
    else: # Sinon (dans tous les autres cas)
        print("bonjour a tous")

print("-------")
greetings(profs_jv)
profs_jv.append("gaetan") # Ajout d'un nom dans la liste des profs
greetings(profs_jv)

# Définition d'une fonction qui augmente le nombre d'élèves jusqu'à un nombre max
def remplir_classe(nb_max):
    global nb_etudiants
    while nb_etudiants < nb_max: # Tant que nb_etudiants < nb_max
        accueil_nouvel_eleve()

remplir_classe(25)

# Dictionaries : ensemble de paires clé/valeur
personne = { 
    "prenom": "brice", 
    "nom": "maurin", 
    "age": 35
}

# Appel de la valeur derrière la clé prénom
print(personne["prenom"])

# Utilisation d'une classe, voir le fichier personne.py
from personne import Personne

# Ici on crée des objets à partir du modèle de la classe
brice = Personne("brice", "maurin", 35)
gaetan = Personne("gaetan", "blaise", 32)

brice.prenom_nom = "yolande hollande"

# Utilisation d'une fonction de classe
brice.se_presenter()
gaetan.se_presenter()