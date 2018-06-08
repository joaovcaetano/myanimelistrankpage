#-*- coding: utf-8 -*-
import pandas as pd
import csv
import networkx as nx
import matplotlib.pyplot as plt
arq = pd.read_csv('bpequena.csv', sep = '\t', header = None)
i = 0
k = 0
j = 0
y = 0
tabela1 = []
while(i<len(arq[0])):#esse while monta tabela
	usuario = arq[0][0]
	if(arq[0][i] == usuario):
		c1 = arq[1][i]
		c2 = arq[2][i]
		tabela1.append([c1,c2])
		i = i + 1
	else:
		break

G = nx.DiGraph()
while(j<len(tabela1)):#esse while cria os nós
	G.add_node(tabela1[j][0])
	j = j + 1

while(k<len(tabela1)):#esse while cria as arestas
	y = 0
	while(y<len(tabela1)):
		if(y == k):
			y = y + 1
		else:
			#G.add_edges_from([(tabela1[k][0], tabela1[y][0])])
			G.add_weighted_edges_from([(tabela1[y][0],tabela1[k][0],0)])
			y = y + 1
	k = k + 1
i = 0
j = 1
while(i<len(tabela1)):
	while(j<len(tabela1)):
		if(tabela1[i][1] < tabela1[j][1]):
			print "\nDEU - 1"
			print str(tabela1[i][0]) + "," + str(tabela1[j][0])
			new_value_weight = tabela1[j][1] - tabela1[i][1]
			print G[tabela1[j][0]][tabela1[i][0]]['weight']+new_value_weight
			G.add_weighted_edges_from([(tabela1[j][0],tabela1[i][0],(G[tabela1[j][0]][tabela1[i][0]]['weight']+new_value_weight))])
			j = j + 1
		elif(tabela1[i][1] == tabela1[j][1]):
			j = j + 1
		else:
			print "\nDEU - 2"
			print str(tabela1[i][0]) + "," + str(tabela1[j][0])
			new_value_weight = tabela1[i][1] - tabela1[j][1]
			print G[tabela1[i][0]][tabela1[j][0]]['weight']+new_value_weight
			G.add_weighted_edges_from([(tabela1[i][0],tabela1[j][0],(G[tabela1[i][0]][tabela1[j][0]]['weight']+new_value_weight))])
			j = j + 1
	i = i + 1
	j = i+1

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrows=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()
