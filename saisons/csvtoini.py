#!/usr/bin/python3
# -*-coding:Utf-8 -*

import os
import csv
import configparser

"""

Script pour créer automatiquement les ini à partir des csv

Premier test 	: créer manuellement test.ini 				: OK
Deuxième test	: créer manuellement 20.ini 				: OK
Troisième test	: remplir automatiquement 20.ini 			: NOK
Quatrième test 	: créer et remplire automatiquement 20.ini	:

Il faudrait modifier les csv en remplaçant le sépérateur de ',' à ";"

"""

path = "/home/thomas/Data/Python/South Park/saisons"
os.chdir(path)

# on initialise un fichier ini
fichier_ini = configparser.ConfigParser()

# on charge le fichier csv
saison_csv = ""
with open ("20.csv","r") as fichier_csv:
	fichier_reader = csv.reader(fichier_csv)
	for row in fichier_reader:
		saison_csv = saison_csv + str(row)

# on crée la première clef
fichier_ini['saison'] = {}
fichier_ini['saison']['num_saison'] = ""
fichier_ini['saison']['nb_episodes'] = ""
fichier_ini['saison']['chemin'] = ""

# on crée les autres clefs
fichier_ini['episode_1'] = {}
fichier_ini['episode_1']['nom_episode'] = ""
fichier_ini['episode_1']['num_episode'] = ""
fichier_ini['episode_1']['nb_vues'] = ""
fichier_ini['episode_1']['derniere_vue'] = ""
fichier_ini['episode_1']['double'] = ""

fichier_ini['episode_2'] = {}
fichier_ini['episode_2']['nom_episode'] = ""
fichier_ini['episode_2']['num_episode'] = ""
fichier_ini['episode_2']['nb_vues'] = ""
fichier_ini['episode_2']['derniere_vue'] = ""
fichier_ini['episode_2']['double'] = ""

fichier_ini['episode_3'] = {}
fichier_ini['episode_3']['nom_episode'] = ""
fichier_ini['episode_3']['num_episode'] = ""
fichier_ini['episode_3']['nb_vues'] = ""
fichier_ini['episode_3']['derniere_vue'] = ""
fichier_ini['episode_3']['double'] = ""

fichier_ini['episode_4'] = {}
fichier_ini['episode_4']['nom_episode'] = ""
fichier_ini['episode_4']['num_episode'] = ""
fichier_ini['episode_4']['nb_vues'] = ""
fichier_ini['episode_4']['derniere_vue'] = ""
fichier_ini['episode_4']['double'] = ""

fichier_ini['episode_5'] = {}
fichier_ini['episode_5']['nom_episode'] = ""
fichier_ini['episode_5']['num_episode'] = ""
fichier_ini['episode_5']['nb_vues'] = ""
fichier_ini['episode_5']['derniere_vue'] = ""
fichier_ini['episode_5']['double'] = ""

fichier_ini['episode_6'] = {}
fichier_ini['episode_6']['nom_episode'] = ""
fichier_ini['episode_6']['num_episode'] = ""
fichier_ini['episode_6']['nb_vues'] = ""
fichier_ini['episode_6']['derniere_vue'] = ""
fichier_ini['episode_6']['double'] = ""

fichier_ini['episode_7'] = {}
fichier_ini['episode_7']['nom_episode'] = ""
fichier_ini['episode_7']['num_episode'] = ""
fichier_ini['episode_7']['nb_vues'] = ""
fichier_ini['episode_7']['derniere_vue'] = ""
fichier_ini['episode_7']['double'] = ""

fichier_ini['episode_8'] = {}
fichier_ini['episode_8']['nom_episode'] = ""
fichier_ini['episode_8']['num_episode'] = ""
fichier_ini['episode_8']['nb_vues'] = ""
fichier_ini['episode_8']['derniere_vue'] = ""
fichier_ini['episode_8']['double'] = ""

fichier_ini['episode_9'] = {}
fichier_ini['episode_9']['nom_episode'] = ""
fichier_ini['episode_9']['num_episode'] = ""
fichier_ini['episode_9']['nb_vues'] = ""
fichier_ini['episode_9']['derniere_vue'] = ""
fichier_ini['episode_9']['double'] = ""

fichier_ini['episode_10'] = {}
fichier_ini['episode_10']['nom_episode'] = ""
fichier_ini['episode_10']['num_episode'] = ""
fichier_ini['episode_10']['nb_vues'] = ""
fichier_ini['episode_10']['derniere_vue'] = ""
fichier_ini['episode_10']['double'] = ""

# on écrit le fichier
with open('20.ini','w') as saison:
	fichier_ini.write(saison)
