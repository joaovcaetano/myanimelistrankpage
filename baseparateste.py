#-*- coding: utf-8 -*-
import pandas as pd
import csv
import sys


arq = pd.read_csv('basemenor.csv', sep = ';', header = None)
i = 0
c = 1000
base = 'basefinal.csv'

csv_modificado = open(base, "wb")
writer = csv.writer(csv_modificado, delimiter='\t')
tabelaFinal = []
tabela = []
while(i<len(arq[0]) and len(tabelaFinal) < 1000):
	if i>1000:	
		c = c + 1000
	u0 = arq[0][i]
	tabela = []
	while(i<len(arq[0])):#esse while monta tabela
		if(arq[0][i] == u0):
			if arq[1][i]<500:
				u1 = arq[1][i]
				u2 = arq[2][i]
				tabela.append([u0,u1,u2])
			i = i + 1
		else:
			break
	if len(tabela) > 100:
		tabelaFinal.append(tabela)
		print str(len(tabelaFinal)) + "AGR"
i = 0
j = 0
while(i<len(tabelaFinal)):
	if i > c:
		print i
		c = c+1000
	dados = []
	dados = tabelaFinal[i]
	print j
	j = 0
	while j < len(dados):
		writer.writerow(dados[j])
		j = j+1
	i = i+1
