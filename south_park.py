#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""

Problème de formatage du nom de l'épisode, mais sinon ça fonctionne.

"""

import saisons
import os
import csv
from random import randint
from subprocess import Popen

print("Bienvenue dans la sélection aléatoire d'un épisode de South Park\n")
print("Deux façons de l'utiliser : ")
print("    - (1) l'application définit directement un épisode")
print("    - (2) vous indiquez d'abord de combien de saisons vous disposez, puis le nombre d'épisodes dans la saison définie par l'application\n")

choix = int(input("De quelle façon voulez-vous utiliser l'application ? (1/2)")) # Raise Error si mauvais choix de l'utilisateur-rice
reponse = 'n'
while reponse == 'n':
	if choix == 1:
		saison = str(randint(1,18))
		season = int(saison)
		if len(saison) == 1:
			saison = '0' + saison
		else:
			saison = saison
		saison = saison + ".csv"
		path = "/home/thomas/Data/Python/South Park/saisons"
		os.chdir(path)
		fichier = open(saison, "rb") # penser à os.chdir(./saisons), mais le "./" n'est pas reconnu pas Python...
		ligne = fichier.readlines()
		nb_episodes = len(ligne) - 1
		episode = randint(1,nb_episodes)
		ligne_episode = str(ligne[episode])
		ligne_episode = ligne_episode.split(",")
		nom_episode = ligne_episode[1] # il y a un problème de formatage du nom, des '\' aparaissent. Il doit y avoir un moyen de les supprimers en parcourant la chaine)
	if choix == 2:
		print("\nNous allons tout d'abord sélectionner une saison, puis un épisode dans cette saison.\n")
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
			# Raise Error si pas int
			saison_max = input("Quelle est la dernière saison à votre disposition ?")
			# Raise Error si pas int
			if saison_min >= saison_max:
				print("Une erreur est survenue. Le n° de la première saison est supérieur à celui de la dernière.")
			else:
				season = choix_saison(saison_min,saison_max)
		print("L'application a sélectionné la saison : {}\n".format(season))

		print("Sélection de l'épisode")	
		episode_min = 1
		episode_max = input("Combien d'épisodes contient la saison {} ?".format(season))
		episode = choix_episode(episode_min,episode_max)
		print("L'application a sélectionné l'épisode : {}\n".format(episode))
		saison = str(season)
		if len(saison) == 1:
			saison = '0' + saison
		else:
			saison = saison			
		saison = saison + ".csv"
		path = "/home/thomas/Data/Python/South Park/saisons"
		os.chdir(path)
		fichier = open(saison, "rb") # penser à os.chdir(./saisons), mais le "./" n'est pas reconnu pas Python...
		ligne = fichier.readlines()
		ligne_episode = str(ligne[episode])
		ligne_episode = ligne_episode.split(",")
		nom_episode = ligne_episode[1] # il y a un problème de formatage du nom, des '\' aparaissent. Il doit y avoir un moyen de les supprimers en parcourant la chaine)

	
	print("L'application a définie l'épisode {}, n°{}, de la saison {}".format(nom_episode,episode,season))
	fichier.close()
	
	
	reponse = input("Cela vous convient-il ? o/n") #prévoir les majuscules

print("\nBon visionnage ;-)")
