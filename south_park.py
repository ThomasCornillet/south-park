#!/usr/bin/python3
# -*-coding:Utf-8 -*

# features à ajouter : rentrer les informations du nombre d'épisodes dans chaque saison pour éviter de demander le nombre d'épisodes
# raise error si pas d'entier entré
# gérer le cas où la personne a une saison manquante (du genre 1-5,6-8)
# peut-être prévoir le cas ou la personne veut une saison en particulier

"""et pour quoi pas poser une dernière question (est-ce que ça vous convient ?) et si oui, lancer directement l'épisode dans vlc
pour se faire, voir la commande os.popen()
si je fais ça, il faudrait que je renomme tous les épisodes avec des noms générique
voir faire une base de données avec les noms des fichiers, et pas besoin de renommer
enfin une "base de données", faire une fichier csv avec tous les épisodes ? ou un fichier csv par saison ? (ce qui permettrait de connaitre automatiquement le nombre d'épisodes de la saison
si choix d'un csv, possibilité de mettre un incrémentateur pour pondérer les épisodes enfonction des vues"""

from random import randint
from subprocess import Popen

print("Bienvenue dans la sélection aléatoire d'un épisode de South Park\n")
print("Nous allons tout d'abord sélectionner une saison, puis un épisode dans cette saison.\n")

def choix_saison(a,b):
	a = int(a)
	b = int(b)
	return randint(a,b)

def choix_episode(c,d):
	c = int(c)
	d = int(d)
	return randint(c,d)

print("Sélection de la saison")
saison_min = 2
saison_max = 1
while saison_min >= saison_max:
	saison_min = input("Quelle est la première saison à votre disposition ?")
	saison_max = input("Quelle est la dernière saison à votre disposition ?")
	if saison_min >= saison_max:
		print("Une erreur est survenue. Le n° de la première saison est supérieur à celui de la dernière.")
	else:
		saison_choix = choix_saison(saison_min,saison_max)
print("L'application a sélectionné la saison : {}\n".format(saison_choix))

print("Sélection de l'épisode")
episode_min = 1
episode_max = input("Combien d'épisodes contient la saison {} ?".format(saison_choix))
episode_choix = choix_episode(episode_min,episode_max)
print("L'application a sélectionné l'épisode : {}\n".format(episode_choix))

print("Vous vous apprêtez à regarder l'épisode {} de la saison {} de South Park.".format(episode_choix,saison_choix))
reponse = input("Cela vous convient-il ? o/n") #prévoir les majuscules
if reponse == 'o':
	print("L'épisode va se lancer.\n")
	print("Bon visionnage ;-)")
if reponse == 'n':
	print("Très bien. Nous allons recommencer le processus de sélection.\n")
	# prévoir le retour, surement avec des boucles
#elif
	# print("Je ne comprends pas votre réponse")
	# prévoir de poser la question à nouveau
