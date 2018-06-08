#-*- coding: utf-8 -*-
import pandas as pd
import csv
import sys


arq = pd.read_csv('rating.csv', header = None)
i = 1
base = 'basemenor.csv'
count = 0
csv_modificado = open(base, "wb")
writer = csv.writer(csv_modificado, delimiter=';')
while(i<len(arq[0])):
	if((int(arq[2][i])) != -1):
		dados = []
		dados.append(int(arq[0][i]))
		dados.append(int(arq[1][i]))
		dados.append(int(arq[2][i]))
		writer.writerow(dados)
	i = i+1



