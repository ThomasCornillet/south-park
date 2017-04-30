#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""

Ceci est la première version de l'application.

Elle n'est pas tout à fait stable (voir bugs connus), mais elle fonctionne.

Je fais une branche pour avoir une sauvegarde de cette version. 
La prochaine version ne fera pas l'objet d'une branche mais sera développé dans master.
Elle ne proposera plus le choix de la méthode de sélection, assumant que l'utilisateur-rice possède toutes les saisons et tous les épisodes.


Bugs connus : 
	- formatage du nom de l'épisode
	- si les noms d'épisodes contiennent des virgules ','
		mauvais split pour ligne_episode

"""

import saisons # je ne suis pas sur que ça serve à quelque chose... (en tout cas, ça n'empêche pas de devoir faire un os.chdir() pour rentrer dans le dossier saisons
import os
import csv
from random import randint
from subprocess import Popen

print("Bienvenue dans la sélection aléatoire d'un épisode de South Park\n")
print("Deux façons de l'utiliser : ")
print("    - (1) l'application définit directement un épisode")
print("    - (2) vous indiquez d'abord de combien de saisons vous disposez, puis le nombre d'épisodes dans la saison définie par l'application\n")

choix = input("De quelle façon voulez-vous utiliser l'application ? (1/2)\n")
while choix != '1' and choix != '2':
	print("Je ne comprends pas.")
	print("Veuillez entrer 1 ou 2\n")
	choix = input("De quelle façon voulez-vous utiliser l'application ? (1/2)\n")
choix = int(choix)
reponse = 'n'
while reponse == 'n':
	if choix == 1:
		saison = str(randint(1,20))
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
		fichier.close()
		nb_episodes = len(ligne) - 1
		episode = randint(1,nb_episodes)
		ligne_episode = str(ligne[episode])
		ligne_episode = ligne_episode.split(",")
		nom_episode = ligne_episode[1] 
	else:
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
		saison_min = input("Quelle est la première saison à votre disposition ?\n")
		while saison_min != '1' and saison_min != '2' and saison_min != '3' and saison_min != '4' and saison_min != '5' and saison_min != '6' and saison_min != '7' and saison_min != '8' and saison_min != '9' and saison_min != '10' and saison_min != '11' and saison_min != '12' and saison_min != '13' and saison_min != '14' and saison_min != '15' and saison_min != '16' and saison_min != '17' and saison_min != '18' and saison_min != '19' and saison_min != '20':
			print("Je ne comprends pas.")
			print("Veuillez entrer un numéro de saison valide, de 1 à 20")
			saison_min = input("Quelle est la première saison à votre disposition ?\n")
		saison_max = input("Quelle est la dernière saison à votre disposition ?")
		while saison_max != '1' and saison_max != '2' and saison_max != '3' and saison_max != '4' and saison_max != '5' and saison_max != '6' and saison_max != '7' and saison_max != '8' and saison_max != '9' and saison_max != '10' and saison_max != '11' and saison_max != '12' and saison_max != '13' and saison_max != '14' and saison_max != '15' and saison_max != '16' and saison_max != '17' and saison_max != '18' and saison_max != '19' and saison_max != '20':
			print("Je ne comprends pas.")
			print("Veuillez entrer un numéro de saison valide, de 1 à 20")
			saison_max = input("Quelle est la dernière saison à votre disposition ?")
		season = choix_saison(saison_min,saison_max)
		print("L'application a sélectionné la saison : {}\n".format(season))
	
		print("Sélection de l'épisode")	
		episode_min = 1
		path = "/home/thomas/Data/Python/South Park/saisons"
		os.chdir(path)
		saison = str(season)
		if len(saison) == 1:
			saison = '0' + saison
		else:
			saison = saison			
		saison = saison + ".csv"
		fichier = open(saison, "rb")
		ligne = fichier.readlines()
		fichier.close()
		episode_max = len(ligne) - 1
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
		fichier.close()
		nb_episodes = len(ligne) - 1
		ligne_episode = str(ligne[episode])
		ligne_episode = ligne_episode.split(",")
		nom_episode = ligne_episode[1]

	print("L'application a sélectionné l'épisode {}, n°{}/{}, de la saison {}\n".format(nom_episode,episode,nb_episodes,season))
	
	nb_vues = int(ligne_episode[4])
	if nb_vues == 0:
		print("Vous n'avez pas encore vu cet épisode.\n")
	else:
		print("Vous avez déjà vu cet épisode {} fois\n".format(nb_vues))
	
	# on veut tester maintenant si l'épisode se trouve dans un arc narratif
	
	# on définit les valeurs de deux épisodes antérieurs et deux deux d'après
	# mais on ne les charge pas encore, au cas où il y ait un IndexError
	ep_ant = episode - 1
	ep_ant2 = ep_ant - 1
	ep_apr = episode + 1
	ep_apr2 = episode + 2
	
	# on charge la variable double de l'épisode sélectionné
	double = ligne_episode[3]
	
	if double == "True":
		print("Attention, l'épisode sélectionné fait partie d'un arc narratif")

		if episode == 1:
			# c'est le premier de la saison
			# on charge donc l'épisode d'après
			ligne_ep_apr = str(ligne[ep_apr])
			ligne_ep_apr = ligne_ep_apr.split(",")
			double_apr = ligne_ep_apr[3]
			# et l'épisode encore d'après
			ligne_ep_apr2 = str(ligne[ep_apr2])
			ligne_ep_apr2 = ligne_ep_apr2.split(",")
			double_apr2 = ligne_ep_apr2[3]
			
			if double_apr2 == "True":
				print("Il s'agit du premier épisode d'une \"trilogie\".\n")
			else:
				print("Il s'agit de la première partie d'un double épisode\n")
				
		elif episode == 2:
			# c'est le deuxième de la saison
			# on charge l'épisode antérieur
			ligne_ep_ant = str(ligne[ep_ant])
			ligne_ep_ant = ligne_ep_ant.split(",")
			double_ant = ligne_ep_ant[3]
			# on charge donc l'épisode d'après
			ligne_ep_apr = str(ligne[ep_apr])
			ligne_ep_apr = ligne_ep_apr.split(",")
			double_apr = ligne_ep_apr[3]
			# et l'épisode encore d'après
			ligne_ep_apr2 = str(ligne[ep_apr2])
			ligne_ep_apr2 = ligne_ep_apr2.split(",")
			double_apr2 = ligne_ep_apr2[3]
			
			if double_ant == "True":
				if double_apr == "True":
					print("Il s'agit du deuxième épisode d'une \"trilogie\".\n")
				else:
					print("Il s'agit de la deuxième partie d'un double épisode\n")
			else:
				if double_apr2 == "True":
					print("Il s'agit du premier épisode d'une \"trilogie\".\n")
				else:
					print("Il s'agit de la première partie d'un double épisode\n")
	
		elif episode == nb_episodes:
			# c'est le dernier de la saison
			# on charge l'épisode antérieur
			ligne_ep_ant = str(ligne[ep_ant]) 
			ligne_ep_ant = ligne_ep_ant.split(",")
			double_ant = ligne_ep_ant[3]
			# on charge l'épisode antérieur à l'épisode antérieur
			ligne_ep_ant2 = str(ligne[ep_ant2])
			ligne_ep_ant2 = ligne_ep_ant2.split(",")
			double_ant2 = ligne_ep_ant2[3]
			
			if double_ant2 == "True":
				print("Il s'agit du dernier épisode d'une \"trilogie\".\n")
			else:
				print("Il s'agit de la deuxième partie d'un double épisode\n")
		
		elif episode == nb_episodes - 1:
			# c'est l'avant dernier de la saison
			# on charge l'épisode antérieur
			ligne_ep_ant = str(ligne[ep_ant])
			ligne_ep_ant = ligne_ep_ant.split(",")
			double_ant = ligne_ep_ant[3]
			# on charge l'épisode antérieur à l'épisode antérieur
			ligne_ep_ant2 = str(ligne[ep_ant2])
			ligne_ep_ant2 = ligne_ep_ant2.split(",")
			double_ant2 = ligne_ep_ant2[3]
			# on charge donc l'épisode d'après
			ligne_ep_apr = str(ligne[ep_apr])
			ligne_ep_apr = ligne_ep_apr.split(",")
			double_apr = ligne_ep_apr[3]
			
			if double_apr == "True":
				if double_ant == "True":
					print("Il s'agit du deuxième épisode d'une \"trilogie\".\n")
				else:
					print("Il s'agit de la première partie d'un double épisode\n")
			else:
				if double_ant2 == "True":
					print("Il s'agit du dernier épisode d'une \"trilogie\".\n")
				else:
					print("Il s'agit de la deuxième partie d'un double épisode\n")
		
		else:
			# on charge l'épisode antérieur
			ligne_ep_ant = str(ligne[ep_ant]) 
			ligne_ep_ant = ligne_ep_ant.split(",")
			double_ant = ligne_ep_ant[3]
			# on charge l'épisode antérieur à l'épisode antérieur
			ligne_ep_ant2 = str(ligne[ep_ant2])
			ligne_ep_ant2 = ligne_ep_ant2.split(",")
			double_ant2 = ligne_ep_ant2[3]
			# on charge donc l'épisode d'après
			ligne_ep_apr = str(ligne[ep_apr])
			ligne_ep_apr = ligne_ep_apr.split(",")
			double_apr = ligne_ep_apr[3]
			# et l'épisode encore d'après
			ligne_ep_apr2 = str(ligne[ep_apr2])
			ligne_ep_apr2 = ligne_ep_apr2.split(",")
			double_apr2 = ligne_ep_apr2[3]
	
			if double_ant2 == "True":
				print("Il s'agit du dernier épisode d'une \"trilogie\".\n")
			elif double_apr2 == "True":
				print("Il s'agit du premier épisode d'une \"trilogie\".\n")
			elif double_ant == "True" and double_apr == "True":
				print("Il s'agit du deuxième épisode d'une \"trilogie\".\n")
			elif double_ant == "False" and double_apr2 == "False":
				print("Il s'agit de la première partie d'un double épisode\n")
			elif double_apr == "False" and double_ant2 == "False":
				print("Il s'agit de la deuxième partie d'un double épisode\n")

	reponse = input("Cela vous convient-il ? o/n\n")
	reponse = reponse.lower()
	while reponse != 'o' and reponse != 'n':
		print("Je ne comprends pas.")
		print("Veuillez entrer o ou n\n")
		reponse = input("Cela vous convient-il ? o/n\n")
		reponse = reponse.lower()

print("\nBon visionnage ;-)")
