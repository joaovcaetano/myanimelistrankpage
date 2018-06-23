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
qtd = 30
threshold = 0.3
k=0
arqUsers = []
while(k<qtd):
	userAtual = arquivos[k]
	arq = pd.read_csv(userAtual, sep = '\t', header = None)
	#leitura do user em uma tabela
	i = 0
	count = 0
	tabelaFinal = []
	tabela = []
	if(arq[0][0] not in vertices):
		vertices.append(arq[0][i])
		#G.add_vertices(int(arq[0][0]))
	print "first while" + str(k)
	while(i<len(arq[0])):#esse while monta tabela
		tabela.append([arq[1][i]])
		#tabelaFinal.append([u0,u1,u2])
		i = i+1
	i = k + 1
	#print "big while"
	while(i<qtd):
		tabelaAux = []
		arqAux = pd.read_csv(arquivos[i], sep = '\t', header = None)
		j =0
		if(arqAux[0][0] not in vertices):
			vertices.append(arqAux[0][0])
		count = 0
		while(j<len(arqAux[0])):#esse while monta tabela
			tabelaAux.append([arqAux[1][j]])
			if arqAux[1][j] in tabela:
				count = count +1
			j = j+1
		j = 0
		if count > len(tabelaAux)*threshold:
			edges.append((k,i))
			weight.append(count)
			#G.add_edge(int(arq[0][0]),int(arqAux[0][0]),weight = count)
		i = i + 1
	i = 0
	j = 0
	k = k + 1
print "community"
G = Graph(vertex_attrs={"label": vertices}, edges=edges)
comms = G.community_leading_eigenvector(clusters=10)
listCommun = list(comms)



i = 0
j = 0
k = 0
while(i<len(listCommun)):
	base = "communities/com"+str(i)+".csv"
	csv_modificado = open(base, "wb")
	writer = csv.writer(csv_modificado, delimiter='\t')
	j = 0
	while(j<len(listCommun[i])):
		arquivoSaida = pd.read_csv("users/"+str(vertices[listCommun[i][j]])+'.csv', sep = '\t', header = None)
		k = 0
		while(k < len(arquivoSaida[0])):
			dados = []
			dados.append(arquivoSaida[0][k])
			dados.append(arquivoSaida[1][k])
			dados.append(arquivoSaida[2][k])
			writer.writerow(dados)
			k = k+1
		j = j+1
	i = i+1

"""print plot
plot(comms, mark_groups = True,layout = "fr")"""