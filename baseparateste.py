#-*- coding: utf-8 -*-
import pandas as pd
import csv
import sys


arq = pd.read_csv('basemenor.csv', sep = ';', header = None)
i = 1
c = 1000
base = 'baseteste.csv'
count = 0
csv_modificado = open(base, "wb")
writer = csv.writer(csv_modificado, delimiter='\t')
while(i<len(arq[0])):
	if i > c:
		print i
		c = c+1000
	if((int(arq[1][i])) < 200):
		dados = []
		dados.append(int(arq[0][i]))
		dados.append(int(arq[1][i]))
		dados.append(int(arq[2][i]))
		writer.writerow(dados)
	i = i+1