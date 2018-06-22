#-*- coding: utf-8 -*-
import pandas as pd
import csv
import sys
import os
from igraph import *
pasta = "users"
caminhos = [os.path.join(pasta,nome) for nome in os.listdir(pasta)]
arquivos = [ar for ar in caminhos if os.path.isfile(ar)]
#definir user atual
G = Graph()
k=0
arqUsers = []
tabela_de_nos = []
while(k<len(arquivos)):
	userAtual = arquivos[k]
	arq = pd.read_csv(userAtual, sep = '\t', header = None)
	#leitura do user em uma tabela
	i = 0
	count = 0
	tabelaFinal = []
	tabela = []
	if(arq[0][0] not in tabela_de_nos):
		G.add_vertices(arq[0][0])
		tabela_de_nos.append(arq[0][i])
	print "first while"
	while(i<len(arq[0])):#esse while monta tabela
		tabela.append([arq[1][i]])
		#tabelaFinal.append([u0,u1,u2])
		i = i+1
	y = k + 1
	print "big while"
	while(y<len(arquivos)):
		tabelaAux = []
		arqAux = pd.read_csv(arquivos[y], sep = '\t', header = None)
		j = 0
		if(arqAux[0][0] not in tabela_de_nos):
			G.add_vertices(arqAux[0][0])
			tabela_de_nos.append(arqAux[0][0])
		count = 0
		while(j<len(arqAux[0])):#esse while monta tabela
			tabelaAux.append([arqAux[1][j]])
			if arqAux[1][j] in tabela:
				count = count +1
			j = j+1
		j = 0
		if count > len(tabelaAux)*2.0/4.0:
			G.add_edge(arq[0][0], arqAux[0][0], weight = count)
		y = y + 1
	i = 0
	j = 0
	k = k + 1
comms = G.community_multilevel()
plot(comms, mark_groups = True)