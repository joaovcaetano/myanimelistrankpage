#-*- coding: utf-8 -*-
import pandas as pd
import csv
import sys


arq = pd.read_csv('basefinal.csv', sep = '\t', header = None)
i = 0
#c = 1000
tabelaFinal = []
tabela = []
while(i<len(arq[0])):
	print i
	u0 = arq[0][i]
	base = "users/user"+str(u0)+".csv"
	csv_modificado = open(base, "wb")
	writer = csv.writer(csv_modificado, delimiter='\t')
	tabela = []
	j =0
	while(i<len(arq[0])):#esse while monta tabela
		print i
		if(arq[0][i] == u0):
			u1 = arq[1][i]
			u2 = arq[2][i]
			tabela.append([u0,u1,u2])
			writer.writerow(tabela[j])
			j = j+1
			i = i + 1
		else:
			break
