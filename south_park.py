#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""

Bugs en cours : 
	- formatage du nom de l'épisode

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
			if saison_min > saison_max:
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
		nb_episodes = len(ligne) - 1
		ligne_episode = str(ligne[episode])
		ligne_episode = ligne_episode.split(",")
		nom_episode = ligne_episode[1]

	print("L'application a défini l'épisode {}, n°{}/{}, de la saison {}\n".format(nom_episode,episode,nb_episodes,season))
	
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
	
		# on veut alors voir sa place dans l'arc narratif, et s'il s'agit d'un double épisode ou d'une trilogie
		# mais avant ça, il faut voir si les deux épisodes d'avant et les deux épisodes d'après existe
		# pour l'instant, je l'ai fait avec des try, on va essayer autrement
		
		# le nombre d'épisode est contenue dans la variable nb_episodes
		# on peut essayer de déterminer la place de l'épisode dans la saison
		# d'abord s'il est en début de saison (premier ou deuxième), ce qui voudrait dire que ep_ant ou ep_ant2 n'existent pas
		# mais ça on peut le savoir avec le numéro de l'épisode variable episode
		if episode == 1:
			# c'est le premier de la saison
			# alors ni ep_ant, ni ep_ant2 n'existent
			# mais par contre, ep_apr et ap_apr2 existent, on peut donc les charger
			# on charge donc l'épisode d'après
			ligne_ep_apr = str(ligne[ep_apr])
			ligne_ep_apr = ligne_ep_apr.split(",")
			double_apr = ligne_ep_apr[3]
			# et l'épisode encore d'après
			ligne_ep_apr2 = str(ligne[ep_apr2])
			ligne_ep_apr2 = ligne_ep_apr2.split(",")
			double_apr2 = ligne_ep_apr2[3]
			
			# on cherche à déterminer si c'est le permier d'un double ou le premier d'une trilogie
			if double_apr2 == "True":
				print("Il s'agit du premier épisode d'une \"trilogie\".\n")
			else:
				print("Il s'agit de la première partie d'un double épisode\n")
				
		elif episode == 2:
			# c'est le deuxième de la saison
			# ep_ant 2 n'existe pas
			# mais ep_ant, ep_apr et ep_apr2 existent, on peut donc les charger
			# on charge l'épisode antérieur
			ligne_ep_ant = str(ligne[ep_ant]) # je ne sais pas si c'est nécessaire de la redéfinir après l'avoir testée
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
			
			# on cherche à déterminer si c'est le deuxième d'une trilogie, le dernier d'un double, le premier d'un double ou le premier d'une trilogie
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
			# c'est donc le dernier de la saison, ep_apr et ep_apr2 n'existent pas
			# mais ep_ant et ep_ant2 existent, on peut donc les charger
			# on charge l'épisode antérieur
			ligne_ep_ant = str(ligne[ep_ant]) # je ne sais pas si c'est nécessaire de la redéfinir après l'avoir testée
			ligne_ep_ant = ligne_ep_ant.split(",")
			double_ant = ligne_ep_ant[3]
			# on charge l'épisode antérieur à l'épisode antérieur
			ligne_ep_ant2 = str(ligne[ep_ant2])
			ligne_ep_ant2 = ligne_ep_ant2.split(",")
			double_ant2 = ligne_ep_ant2[3]
			
			# on cherche à déterminer si c'est le dernier d'un double ou le dernier d'une trilogie
			if double_ant2 == "True":
				print("Il s'agit du dernier épisode d'une \"trilogie\".\n")
			else:
				print("Il s'agit de la deuxième partie d'un double épisode\n")
		
		elif episode == nb_episodes - 1:
			# c'est donc l'avant dernier de la saison, ep_apr2 n'existe pas
			# mais ep_ant, ep_ant2 et ep_apr existent, on peut donc les charger
			# on charge l'épisode antérieur
			ligne_ep_ant = str(ligne[ep_ant]) # je ne sais pas si c'est nécessaire de la redéfinir après l'avoir testée
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
			
			# on cherche à déterminer si c'est le premier d'un double, le dernier d'un double, le dernier d'une trilogie ou le deuxième d'une trilogie
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
			# c'est ni le premier, ni le deuxième, ni le dernier, ni l'avant dernier
			# toutes les variables existent, on peut donc les charger
			# on charge l'épisode antérieur
			ligne_ep_ant = str(ligne[ep_ant]) # je ne sais pas si c'est nécessaire de la redéfinir après l'avoir testée
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
	
			# on teste tout
			if double_ant2 == "True":
				print("Il s'agit du dernier épisode d'une \"trilogie\".\n")
			if double_apr2 == "True":
				print("Il s'agit du premier épisode d'une \"trilogie\".\n")
			if double_ant == "True" and double_apr == "True":
				print("Il s'agit du deuxième épisode d'une \"trilogie\".\n")
			if double_ant == "False" and double_apr2 == "False":
				print("Il s'agit de la première partie d'un double épisode\n")
			if double_apr == "False" and double_ant2 == "False":
				print("Il s'agit de la deuxième partie d'un double épisode\n")
	
	fichier.close()
	
	reponse = input("Cela vous convient-il ? o/n\n") #prévoir les majuscules e autres caractères

print("\nBon visionnage ;-)")
