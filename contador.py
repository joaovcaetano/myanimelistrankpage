#-*- coding: utf-8 -*-
import pandas as pd
import csv
arq = pd.read_csv('basemenor.csv',sep= ';', header = None)
i = 0
usuarios = []
j = 0
contador = []
while(i<len(arq[0])):
	if(arq[0][i] not in  usuarios):
		usuarios.append(arq[0][i])
		contador.append(1)
	else:
		while(j<len(usuarios)):
			if(arq[0][i] == usuarios[j]):
				contador[j] = contador[j] + 1
			#print 'j', j
			j = j + 1
	#print 'i', i

	i = i+1

k = 0
csvm = open("contador.csv", "wb")
writer = csv.writer(csv_modificado, delimiter='\t')
while(k<len(usuarios)):
	dados = []
	dados.append(int(usuarios[k]))
	dados.append(int(contador[k]))
	writer.writerow(dados)
