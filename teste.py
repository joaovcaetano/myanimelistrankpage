#-*- coding: utf-8 -*-
import pandas as pd
import csv
import networkx as nx
import matplotlib.pyplot as plt
import re
#arquivo de leitura
arq = pd.read_csv('teste.csv', sep = '\t', header = None)
#indices
i = 0
k = 0
indiceArq = 0
j = 0
y = 0
cont = 1000
#declaracao do grafo
G = nx.DiGraph()
#arquivo de saida
base3 = 'win2.csv'
csv_modificado3 = open(base3, "wb")
writer3 = csv.writer(csv_modificado3, delimiter='\t')
base = 'pagerank.csv'
csv_modificado = open(base, "wb")
writer = csv.writer(csv_modificado, delimiter='\t')
base2 = 'pagerank2.csv'
csv_modificado2 = open(base2, "wb")
writer2 = csv.writer(csv_modificado2, delimiter='\t')
#inicio do codigo
print "lida a base"
while (indiceArq<len(arq[0])):
	if(indiceArq>cont):
		cont = cont + 1000
		print "CHEGOU EM"+str(cont)
	usuario = arq[0][indiceArq]
	tabela1 = []
	while(indiceArq<len(arq[0])):#esse while monta tabela
		if(arq[0][indiceArq] == usuario):
			c1 = arq[1][indiceArq]
			c2 = arq[2][indiceArq]
			tabela1.append([c1,c2])
			indiceArq = indiceArq + 1
		else:
			break
	while(j<len(tabela1)):#esse while cria os nós
		if G.has_node(tabela1[j][0]):
			G.add_node(tabela1[j][0])
		j = j + 1
	i = 0
	j = 1
	while(i<len(tabela1)):
		while(j<len(tabela1)):
			if(tabela1[i][1] < tabela1[j][1]):
				new_value_weight = tabela1[j][1] - tabela1[i][1]
				if(G.has_edge(tabela1[j][0],tabela1[i][0])):
					G.add_weighted_edges_from([(tabela1[j][0],tabela1[i][0],(G[tabela1[j][0]][tabela1[i][0]]['weight']+new_value_weight))])
				else:
					G.add_weighted_edges_from([(tabela1[j][0],tabela1[i][0],(new_value_weight))])
				j = j + 1
			elif(tabela1[i][1] == tabela1[j][1]):
				j = j + 1
			else:
				new_value_weight = tabela1[i][1] - tabela1[j][1]
				if(G.has_edge(tabela1[i][0],tabela1[j][0])):
					G.add_weighted_edges_from([(tabela1[i][0],tabela1[j][0],(G[tabela1[i][0]][tabela1[j][0]]['weight']+new_value_weight))])
				else:
					G.add_weighted_edges_from([(tabela1[i][0],tabela1[j][0],(new_value_weight))])
				j = j + 1
		i = i + 1
		j = i+1	

print "grafo montado"
tabelaSaida = list(G.edges(data='weight'))
i = 0
while(i < len(tabelaSaida)):

	tabelaSaida[i] = list(tabelaSaida[i])
	nodoA = tabelaSaida[i][0]
	nodoB = tabelaSaida[i][1]
	j = i
	while(j < len(tabelaSaida) and (nodoA != tabelaSaida[j][1] or nodoB != tabelaSaida[j][0])):
		j = j+1
	if j<len(tabelaSaida):
		tabelaSaida[j] = list(tabelaSaida[j])
		if tabelaSaida[i][2] > tabelaSaida[j][2]:
			tabelaSaida[i][2] = tabelaSaida[i][2] - tabelaSaida[j][2]
		elif tabelaSaida[j][2] > tabelaSaida[i][2]:
			tabelaSaida[i][1] = nodoA
			tabelaSaida[i][0] = nodoB
			tabelaSaida[i][2] = tabelaSaida[j][2] - tabelaSaida[i][2]
		else:
			tabelaSaida[i][2] = 0
		del tabelaSaida[j]
	tabelaSaida[i][1] = nodoA
	tabelaSaida[i][0] = nodoB
	i = i+1




print "grafo limpo"
#tratamento para sair em tabela
i = 0
while(i<len(tabelaSaida)):
	dados = []
	dados.append(tabelaSaida[i][0])
	dados.append(tabelaSaida[i][1])
	dados.append(tabelaSaida[i][2])
	writer3.writerow(dados)
	i = i+1

"""pos = pos=nx.fruchterman_reingold_layout(G)
plt.axis('auto')
nx.draw_networkx_nodes(G, pos,node_size=20)
nx.draw_networkx_labels(G, pos,alpha=0.4)
nx.draw_networkx_edges(G, pos, arrows=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()"""
