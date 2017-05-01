#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""

south_park.py v2.1 sur branche master

Bugs connus : 

"""

import saisons # je ne suis pas sur que ça serve à quelque chose
import os
import csv
import configparser
from random import randint
from subprocess import Popen # je ne m'en sers pas encore, c'est pour l'ouverture automatique du fichier

print("\nBienvenue dans la sélection aléatoire d'un épisode de South Park\n")
print("L'application va définir aléatoirement un épisode.\n")

path = "/home/thomas/Data/Python/South Park/saisons"
os.chdir(path)

reponse = 'n'
while reponse == 'n':
	saison = str(randint(1,20))
	season = int(saison)
	if len(saison) == 1:
		saison = '0' + saison
	else:
		saison = saison
	saison = saison + ".ini"
	saison_ini = configparser.ConfigParser()
	saison_ini.read(saison)
	nb_episodes = saison_ini['saison']['nb_episodes']
	nb_episodes = int(nb_episodes)
	num_episode = randint(1,nb_episodes)
	if num_episode < 10:
		chemin_episode = str(num_episode)
		chemin_episode = '0' + chemin_episode
	else:
		chemin_episode = str(num_episode)
	chemin_episode = "episode_" + chemin_episode
	nom_episode = saison_ini[chemin_episode]['nom_episode']
	nb_vues = saison_ini[chemin_episode]['nb_vues']
	nb_vues = int(nb_vues)
	
	print("L'application a sélectionné l'épisode {}, n°{}/{}, de la saison {}\n".format(nom_episode,num_episode,nb_episodes,season))
	
	if nb_vues == 0:
		print("Vous n'avez pas encore vu cet épisode.\n")
	else:
		print("Vous avez déjà vu cet épisode {} fois\n".format(nb_vues))

	# on veut tester maintenant si l'épisode se trouve dans un arc narratif
	# on charge la variable double de l'épisode sélectionné
	double = saison_ini[chemin_episode]['double']
	# on charge le n° des épisodes de check de la place dans l'arc
	ep_ant = num_episode - 1
	ep_ant2 = num_episode - 2
	ep_apr = num_episode + 1
	ep_apr2 = num_episode + 2
	if num_episode < 8:
		chemin_ant = "episode_0" + str(ep_ant)
		chemin_ant2 = "episode_0" + str(ep_ant2)
		chemin_apr = "episode_0" + str(ep_apr)
		chemin_apr2 = "episode_0" + str(ep_apr2)
	elif num_episode == 8:
		chemin_ant = "episode_0" + str(ep_ant)
		chemin_ant2 = "episode_0" + str(ep_ant2)
		chemin_apr = "episode_0" + str(ep_apr)
		chemin_apr2 = "episode_" + str(ep_apr2)
	elif num_episode == 9:
		chemin_ant = "episode_0" + str(ep_ant)
		chemin_ant2 = "episode_0" + str(ep_ant2)
		chemin_apr = "episode_" + str(ep_apr)
		chemin_apr2 = "episode_" + str(ep_apr2)
	elif num_episode == 10:
		chemin_ant = "episode_0" + str(ep_ant)
		chemin_ant2 = "episode_0" + str(ep_ant2)
		chemin_apr = "episode_" + str(ep_apr)
		chemin_apr2 = "episode_" + str(ep_apr2)
	elif num_episode == 11:
		chemin_ant = "episode_" + str(ep_ant)
		chemin_ant2 = "episode_0" + str(ep_ant2)
		chemin_apr = "episode_" + str(ep_apr)
		chemin_apr2 = "episode_" + str(ep_apr2)
	else:
		chemin_ant = "episode_" + str(ep_ant)
		chemin_ant2 = "episode_" + str(ep_ant2)
		chemin_apr = "episode_" + str(ep_apr)
		chemin_apr2 = "episode_" + str(ep_apr2)

	if double == "True":
		print("Attention, l'épisode sélectionné fait partie d'un arc narratif")
		
		if num_episode == 1:
			double_apr = saison_ini[chemin_apr]['double']
			double_apr2 = saison_ini[chemin_apr2]['double']
			if double_apr2 == "True":
				print("Il s'agit du premier épisode d'une \"trilogie\".\n")
			else:
				print("Il s'agit de la première partie d'un double épisode\n")
		elif num_episode == 2:
			double_ant = saison_ini[chemin_ant]['double']
			double_apr = saison_ini[chemin_apr]['double']
			double_apr2 = saison_ini[chemin_apr2]['double']
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
		
		elif num_episode == nb_episodes:
			double_ant = saison_ini[chemin_ant]['double']
			double_ant2 = saison_ini[chemin_ant2]['double']
			if double_ant2 == "True":
				print("Il s'agit du dernier épisode d'une \"trilogie\".\n")
			else:
				print("Il s'agit de la deuxième partie d'un double épisode\n")
		
		elif num_episode == nb_episodes - 1:
			double_ant = saison_ini[chemin_ant]['double']
			double_ant2 = saison_ini[chemin_ant2]['double']
			double_apr = saison_ini[chemin_apr]['double']
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
			double_ant = saison_ini[chemin_ant]['double']
			double_ant2 = saison_ini[chemin_ant2]['double']
			double_apr = saison_ini[chemin_apr]['double']
			double_apr2 = saison_ini[chemin_apr2]['double']
			
	reponse = input("Cela vous convient-il ? o/n\n")
	reponse = reponse.lower()
	while reponse != 'o' and reponse != 'n':
		print("Je ne comprends pas.")
		print("Veuillez entrer o ou n\n")
		reponse = input("Cela vous convient-il ? o/n\n")
		reponse = reponse.lower()

print("\nBon visionnage ;-)")
