#!/usr/bin/env python

import csv

file = open('./file.csv', 'r')
reader = csv.DictReader(file, delimiter=';')

liste_releves = []

for row in reader:
	if not row['ff'] == 'mq':
		# conversion de la vitesse du vent de m/s à km/h
		vitesse_vent = 3.6 * float(row['ff'])
	if not row['t'] == 'mq':
		# conversion de la temperature de Kelvin à Celsius
		temperature = float(row['t']) - 273.15
	if not row['u'] == 'mq':
		humidite = int(row['u'])
	if not row['rr1'] == 'mq':
		precipitations  = float(row['rr1'])
		
	liste_releves.append({'id': row['numer_sta'],
	                      'vitesse_vent': vitesse_vent,
	                      'temperature': temperature,
	                      'humidite': humidite,
	                      'precipitations': precipitations})

file.close()


def temperature(releve):
	return releve['temperature']


def temperature_minimale(liste):
	print(liste.sort(key=temperature))
	
	#for releve in liste_releves:
	#	print(releve['temperature'])


temperature_minimale(liste_releves)
