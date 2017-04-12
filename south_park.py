#!/usr/bin/python3
# -*-coding:Utf-8 -*

# raise error si pas d'entier entré
# gérer le cas où la personne a une saison manquante (du genre 1-5,6-8)
# ajouter un avertissement en cas de double ou triple épisodes

import saisons
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

reponse = 'n'

while reponse == 'n':
	print("Sélection de la saison")
	saison_min = 2
	saison_max = 1
	while saison_min >= saison_max:
		saison_min = input("Quelle est la première saison à votre disposition ?")
		# Raise Error si pas int
		saison_max = input("Quelle est la dernière saison à votre disposition ?")
		# Raise Error si pas int
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
#		print("L'épisode va se lancer.\n")
		print("Bon visionnage ;-)")
	if reponse == 'n':
		print("Très bien. Nous allons recommencer le processus de sélection.\n")
