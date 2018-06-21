#-*- coding: utf-8 -*-
import pandas as pd
import csv
import sys
import os
pasta = "users"
caminhos = [os.path.join(pasta,nome) for nome in os.listdir(pasta)]
arquivos = [ar for ar in caminhos if os.path.isfile(ar)]
#definir user atual
userAtual = "users/user11359.csv"
arq = pd.read_csv(userAtual, sep = '\t', header = None)
#leitura do user em uma tabela
i = 0
count = 0
u0 = arq[0][i]
tabelaFinal = []
tabela = []
print "first while"
while(i<len(arq[0])):#esse while monta tabela
	u1 = arq[1][i]
	u2 = arq[2][i]
	tabela.append([u1])
	tabelaFinal.append([u0,u1,u2])
	i = i+1
i = 0
print "big while"
while(i<len(arquivos)):
	tabelaAux = []
	if userAtual != arquivos[i]:
		arqAux = pd.read_csv(arquivos[i], sep = '\t', header = None)
		j =0
		u0 = arqAux[0][j]		
		count = 0
		while(j<len(arqAux[0])):#esse while monta tabela
			u1 = arqAux[1][j]
			u2 = arqAux[2][j]
			tabelaAux.append([u0,u1,u2])
			if u1 in tabela:
				count = count +1
			j = j+1
		j = 0
		if count > len(tabela)*2.0/4.0:
			print u0
			while j < len(tabelaAux):
				tabelaFinal.append(tabelaAux[j])
				j = j+1
	i = i + 1
i = 0
j = 0

base = 'baseCommunity.csv'

csv_modificado = open(base, "wb")
writer = csv.writer(csv_modificado, delimiter='\t')

while(i<len(tabelaFinal)):
	writer.writerow(tabelaFinal[i])
	i = i+1
