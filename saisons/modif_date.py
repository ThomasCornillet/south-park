#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""

Script pour mettre toutes les dernières vues à la même date

"""

import os
import configparser

path = "/home/thomas/Data/Python/South Park/saisons"
os.chdir(path)

date_desiree = ""

i = 1
nb_saisons = 20

while i <= nb_saisons:
	fichier_ini = configparser.ConfigParser()
	saison = str(i)
	season = i
	if len(saison) == 1:
		saison = '0' + saison + ".ini"
	else:
		saison = saison + ".ini"
	fichier_ini.read(saison)
	
	a = 1
	nb_episodes = int(fichier_ini['saison']['nb_episodes'])
	
	while a <= nb_episodes:
		episode = a
		if episode < 10:
			chemin_episode = "episode_0" + str(episode)
		else:
			chemin_episode = "episode_" + str(episode)
		fichier_ini.set(chemin_episode,'derniere_vue',date_desiree)
		fichier_ini.write(open(saison,'w'))
		
		a += 1
	
	i += 1
