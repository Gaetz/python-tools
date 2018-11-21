"""
##########################
# Manipuler des fichiers #
##########################
"""

import os # Needed to use files

# Current working directory
cwd = os.getcwd()

# Create a path for any os 
# (for folders: linux/mac use "/", windows uses "\")
os.path.join(cwd, "Labo", "cobaye.txt")

# Create a folder
os.makedirs("Labo")

# Change directory
os.chdir("Labo") # Relative path

# Absolute path: C:\ArtFx\Cours\Python\python-tools\Labo
# Relative path: .\Labo

# To manipulate absolute paths and relative paths
os.path.abspath(".")
os.path.isabs(".")
os.path.relpath("c:\\ArtFx", ".") # get relative path of first argument from second argument

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
cobaye = open(os.path.join(cwd, "Labo", "cobaye.txt"), "a") # a for append, w for write (will rewrite all file)
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
import shutil

# Copier des fichiers
shutil.copy(os.path.join(cwd, "Labo", "cobaye.txt"), os.path.join(cwd, "Labo", "cobaye2.txt")) # Nouveau nom
shutil.copy(os.path.join(cwd, "Labo", "cobaye.txt"), cwd) # Copie dans un dossier
shutil.copytree(os.path.join(cwd, "Labo", "Exercice"), os.path.join(cwd, "Labo", "Exercice2")) # Copy all files

# Déplacer des fichiers (les dossiers doivent exister)
shutil.move(os.path.join(cwd, "Labo", "cobaye2.txt"), os.path.join(cwd, "Labo", "Exercice"))
shutil.move(os.path.join(cwd, "cobaye.txt"), os.path.join(cwd, "Labo", "cobaye3.txt")) # Renomme après déplacement

# Effacer des fichiers
os.unlink(path) # Efface un fichier
os.rmdir(path) # Efface un dossier vide
os.rmtree(path) # Efface un dossier et tout ce qu'il contient
# Pour envoyer à la corbeille, import send2trash

"""
################
#   Exercice   #
################

Effacer tous les fichiers .txt du dossier Exercice. Puis les recréer avec votre script.
Il faut utiliser os.listdir et filename.endswith('.txt')

"""

