#-*- coding: utf-8 -*-
import pandas as pd
import csv
import sys


arq = pd.read_csv('basemenor.csv', sep = ';', header = None)
i = 0
base = 'basefinal.csv'
basemal = "MyAnimeListData/malsaida.csv"
mal = pd.read_csv(basemal, sep = '\t', header = None)
'''csv_modificado = open(base, "wb")
writer = csv.writer(csv_modificado, delimiter='\t')
k = 0
tabela = []
while(i<len(arq[0])):
	if arq[1][i] in mal[0]:
		u0 = arq[0][i]
		u1 = arq[1][i]
		u2 = arq[2][i]
		tabela.append([u0,u1,u2])
		writer.writerow(tabela[k])
		k = k+1
	i = i + 1
'''