#-*- coding: utf-8 -*-
import pandas as pd
import csv

##Codigo de temporada
'''arquivo = pd.read_csv('anime.csv',delimiter=",",header=None)
arquivo2 = pd.read_csv('fall2015.csv', delimiter = '\t', header = None)
base_saida = 'malsaida.csv'
csv_modificado = open(base_saida, "wb")
writer = csv.writer(csv_modificado, delimiter='\t')
i = 1
fall = []
anime = []
k = 1
for j in range(0,len(arquivo2[0])):
	fall.append(int(arquivo2[0][j]))
while k < len(arquivo[0]):
	anime.append(int(arquivo[0][k]))
	k = k + 1
while(i<len(anime)):
	if anime[i] in fall:
		writer.writerow((anime[i],arquivo[5][i]))
	i = i+1
'''
##Codigo de Gênero
arquivo = pd.read_csv('anime.csv',delimiter=",",header=None)
base = "genero.csv"
csv_modificado = open(base, "wb")
writer = csv.writer(csv_modificado, delimiter = '\t')
anime = []
k = 1
for i in range(0, len(arquivo[0])):
	texto = str(arquivo[2][i])
	texto = texto.split(", ")
	if "Shounen" in texto:
		writer.writerow((arquivo[0][i],arquivo[5][i]))
csv_modificado.close()