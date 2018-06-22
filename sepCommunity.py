#-*- coding: utf-8 -*-
import pandas as pd
import csv
import sys
import os
from igraph import plot
from igraph import *
pasta = "users"
caminhos = [os.path.join(pasta,nome) for nome in os.listdir(pasta)]
arquivos = [ar for ar in caminhos if os.path.isfile(ar)]
#definir user atual
#G = Graph(directed=False)
vertices = []
edges = []
weight = []
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
		vertices.append(arq[0][i])
		#G.add_vertices(int(arq[0][0]))
	print "first while" + str(k)
	while(i<len(arq[0])):#esse while monta tabela
		tabela.append([arq[1][i]])
		#tabelaFinal.append([u0,u1,u2])
		i = i+1
	i = k + 1
	#print "big while"
	while(i<len(arquivos)):
		tabelaAux = []
		arqAux = pd.read_csv(arquivos[i], sep = '\t', header = None)
		j =0
		if(arqAux[0][0] not in tabela_de_nos):
			vertices.append(arqAux[0][0])
		count = 0
		while(j<len(arqAux[0])):#esse while monta tabela
			tabelaAux.append([arqAux[1][j]])
			if arqAux[1][j] in tabela:
				count = count +1
			j = j+1
		j = 0
		if count > len(tabelaAux)*2.0/4.0:
			edges.append((k,i))
			weight.append(count)
			#G.add_edge(int(arq[0][0]),int(arqAux[0][0]),weight = count)
		i = i + 1
	i = 0
	j = 0
	k = k + 1
print "community"
G = Graph(vertex_attrs={"label": vertices}, edges=edges)
comms = G.community_multilevel()
print "plot"
#N = len(tabela_de_nos)
#visual_style["layout"] = G.layout_fruchterman_reingold(weights=G.es["weight"], maxiter=1000, area=N**3, repulserad=N**3
# Plot the graph
plot(comms, mark_groups = True)
