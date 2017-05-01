#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""

Script pour créer automatiquement les ini à partir des csv

Premier test 	: créer manuellement test.ini 				: OK
Deuxième test	: créer manuellement 20.ini 				: OK
Troisième test	: remplir automatiquement 20.ini 			: NOK
Quatrième test 	: créer et remplire automatiquement 20.ini	: OK

Attention, problème avec l'épisode "1%" de le saison 15, le '%' faisant planter configparser
	du coup, il faut l'enlever et l'ajouter manuellement
	sinon, ça fonctionne

"""

import os
import csv
import configparser

path = "/home/thomas/Data/Python/South Park/saisons"
os.chdir(path)

a = 1
nb_saisons = 20

while a <= nb_saisons:

	# on initialise un fichier ini
	fichier_ini = configparser.ConfigParser()

	# on charge le fichier csv
	nom_csv = a
	if a < 10:
		nom_csv = str(nom_csv)
		nom_csv = '0' + nom_csv + ".csv"
	else:
		nom_csv = str(nom_csv)
		nom_csv = nom_csv + ".csv"
	
	saison_csv = ""
	with open (nom_csv,"r") as fichier_csv:
		fichier_reader = csv.reader(fichier_csv, delimiter=';')
		for row in fichier_reader:
			ligne = row
			ligne = ";".join(ligne)
			saison_csv = saison_csv + "/" + ligne
	saison_csv = saison_csv.split("/")
	del saison_csv[0]
	del saison_csv[0]
	fichier_csv.close()
	
	# ici, saison_csv est une liste comportant toutes les informations sur les épisodes de la saison, les inforamtions étant séparées par des ';'
	
	# on crée la première clef
	fichier_ini['saison'] = {}
	fichier_ini['saison']['num_saison'] = str(a)
	nb_episodes = len(saison_csv)
	fichier_ini['saison']['nb_episodes'] = str(nb_episodes)
	fichier_ini['saison']['chemin'] = "" # à emplir à la main

	i = 0
	while i < nb_episodes:
		# on charge l'épisode
		ligne_ep = saison_csv[i]
		ligne_ep = ligne_ep.split(";")
		# on crée le clé épisode dans le fichier ini
		num_ep = "episode_"
		num = ligne_ep[0]
		num_ep = num_ep + str(num)
		fichier_ini[num_ep] = {}
		fichier_ini[num_ep]['nom_episode'] = ligne_ep[1]
		fichier_ini[num_ep]['nb_vues'] = str(ligne_ep[4])
		fichier_ini[num_ep]['derniere_vue'] = ""
		fichier_ini[num_ep]['double'] = ligne_ep[3]
		fichier_ini[num_ep]['chemin'] = ""
		i += 1

	# on écrit le fichier
	nom_ini = a
	if a <10:
		nom_ini = str(nom_ini)
		nom_ini = '0' + nom_ini + ".ini"
	else:
		nom_ini = str(nom_ini)
		nom_ini = nom_ini + ".ini"
	with open(nom_ini,'w') as saison:
		fichier_ini.write(saison)
	saison.close()
	
	a += 1
