#-*- coding: utf-8 -*-
import pandas as pd
import csv
arq = pd.read_csv('pagerank1.csv',sep= '\t', header = None)
base = "normalizado.csv"
csv_modificado = open(base, "wb")
writer = csv.writer(csv_modificado, delimiter='\t')
lista = []
for i in range(0,len(arq[1])):
	u0 = arq[0][i]
	u2 = arq[1][i]
	valor = float(arq[1][i])
	divisao = valor / len(arq[1])
	multiplica = divisao * 9.0
	u1 = multiplica + 1
	lista.append([u0,u2,u1])
	writer.writerow(lista[i])
			
csv_modificado.close()
