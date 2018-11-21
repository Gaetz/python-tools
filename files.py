import shutil
"""
##########################
# Manipuler des fichiers #
##########################
"""

import os  # Needed to use files

# Current working directory
cwd = os.getcwd()

# Create a path for any os
# (for folders: linux/mac use "/", windows uses "\")
os.path.join(cwd, "Labo", "cobaye.txt")

# Create a folder
os.makedirs("Labo")

# Change directory
os.chdir("Labo")  # Relative path

# Absolute path: C:\ArtFx\Cours\Python\python-tools\Labo
# Relative path: .\Labo

# To manipulate absolute paths and relative paths
os.path.abspath(".")
os.path.isabs(".")
# get relative path of first argument from second argument
os.path.relpath("c:\\ArtFx", ".")

# Get folder and filename from a path
os.path.basename(os.path.join(cwd, "Labo", "cobaye.txt"))
os.path.dirname(os.path.join(cwd, "Labo", "cobaye.txt"))

# Content of a folder
os.listdir('C:\\')

# Size of a file
os.path.getsize('C:\\swapfile.sys')

# Path validity
os.path.exists("C:\\swapfile.sys")
os.path.isdir("C:\\swapfile.sys")
os.path.isfile("C:\\swapfile.sys")

# Create / Open a file
# a for append, w for write (will rewrite all file)
cobaye = open(os.path.join(cwd, "Labo", "cobaye.txt"), "a")
cobaye.write("Hello!\n")
cobaye.write("How do you do?\n")
cobaye.close()

# Read a file
cobaye = open(os.path.join(cwd, "Labo", "cobaye.txt"))
content = cobaye.read()
cobaye.close()
print(content)

"""
################
#   Exercice   #
################

1. Créer (en commande python) un dossier Exercice à la racine de votre dossier personnel
2. Créer un fichier paths.txt à la racine de ce dossier
3. Ecrire dans ce fichiers, en passant à la ligne à chaque fois:
    - Le path de 15 fichiers qui s'appellent "data_n.txt", en remplaçant n par un chiffre entre 0 et 14 (inclus)
    - Le path de 3 dossiers appelés "collection_n", en ramplaçant n par un chiffre entre 0 et 2
    - Les paths de 8 fichiers "data_n.txt", situés dans le dossier collection_0, où n est pair et varie entre 0 et 14 (0, 2, 4, ..., 14)
    - Les paths de 7 fichiers "data_n.txt", situés dans le dossier collection_1, où n est impair et varie entre 1 et 13 (1, 3, 5, ..., 13)
    - Les paths de 2 fichiers data_n.txt", situés dans le dossier collection_2, où n est égal à 0 ou à 10
4. Créer ce système de fichier dans votre dossier Exercice
"""


"""
##########################
# Organiser des fichiers #
##########################
"""

# Copier des fichiers
shutil.copy(os.path.join(cwd, "Labo", "cobaye.txt"),
            os.path.join(cwd, "Labo", "cobaye2.txt"))  # Nouveau nom

shutil.copy(os.path.join(cwd, "Labo", "cobaye.txt"),
            cwd)  # Copie dans un dossier

shutil.copytree(os.path.join(cwd, "Labo", "Exercice"),
                os.path.join(cwd, "Labo", "Exercice2"))  # Copy all files

# Déplacer des fichiers (les dossiers doivent exister)
shutil.move(os.path.join(cwd, "Labo", "cobaye2.txt"),
            os.path.join(cwd, "Labo", "Exercice"))

shutil.move(os.path.join(cwd, "cobaye.txt"), os.path.join(
    cwd, "Labo", "cobaye3.txt"))  # Renomme après déplacement

# Effacer des fichiers
os.unlink(path)  # Efface un fichier
os.rmdir(path)  # Efface un dossier vide
os.rmtree(path)  # Efface un dossier et tout ce qu'il contient
# Pour envoyer à la corbeille, import send2trash

"""
################
#   Exercice   #
################

Effacer tous les fichiers .txt du dossier Exercice. Puis les recréer avec votre script.
Il faut utiliser os.listdir et filename.endswith('.txt')

"""

# Parcourir les dossiers, sous-dossiers et fichier d'un répertoire

for folder_name, subfolders, filenames in os.walk(cwd):
    print('The current folder is ' + folder_name)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folder_name + ': ' + filename)

    print('')


"""
############################
# Pattern matching - Regex #
############################
"""

# Exemple. On veut trouver un numéro de téléphone américain de la forme : 333-555-4444

# SANS Regex
def isPhoneNumber(text):
    if len(text) != 12:   
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# AVEC Regex
import re
phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phone_regex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

# Creation de groupes pour récupérer plusieurs valeurs
phone_group_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phone_group_regex.search('My number is 415-555-4242.')
mo.group(1)
mo.group(2)
mo.group(3)
mo.groups()

# Récupération d'une expression OU de l'autre
artfx_regex = re.compile (r'Jeux video|Realisation numerique')

# Element optionel dans un regex
super_regex = re.compile(r'Super(wo)?man')

# {3}: 3 répétition
# *: 0 à n répétitions
# +: 1 à n répétitions

# Regex gourmande ou non
greedy_ha_regex = re.compile(r'(Ha){3,5}')
mo1 = greedy_ha_regex.search('HaHaHaHaHa')
mo1.group()

nongreedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedy_ha_regex.search('HaHaHaHaHa')
mo2.group()

# {,m} 0 to m repetition
# {n,} n to infinite repetition

# find_all("...") instead of search("...") to get multiple results in a list


# \d      Any numeric digit from 0 to 9.
# \D      Any character that is not a numeric digit from 0 to 9.

# \w      Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W      Any character that is not a letter, numeric digit, or the underscore character.

# \s      Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S      Any character that is not a space, tab, or newline.


# Pour récupérer certains caractères seulement :
vowel_regex = re.compile(r'[aeiouAEIOU]')
conson_regex = re.compile(r'[^aeiouAEIOU]')


# Commencer par :
begins_with_hello = re.compile(r'^Hello')
begins_with_hello.search('Hello world!')

# Finir par :
ends_with_number = re.compile(r'\d$')
ends_with_number.search('Your number is 42')

# Wildcard / Joker
at_regex = re.compile(r'.at')
at_regex.findall('The cat in the hat sat on the flat mat.')

"""
#################
#   Exercices   #
#################

1.
Récupérer tout le nom et tout le prénom avec des regex dans la chaîne :
"Prenom: Gaetan     Nom: Blaise-Cazalet"
Utiliser pour cela .*

2.
Créer un regex pour les adresses emails.

"""