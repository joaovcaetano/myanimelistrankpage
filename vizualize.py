#-*- coding: utf-8 -*-
import pandas as pd
import csv
import networkx as nx
import matplotlib.pyplot as plt
import re
#arquivo de leitura
arq = pd.read_csv('win.csv', sep = '\t', header = None)
i = 0
j = 0
#declaracao do grafo
G = nx.DiGraph()
#inicio do codigo
while(j<len(arq[0])): #esse while cria os nós
	G.add_weighted_edges_from([(arq[0][j],arq[1][j],arq[2][j])])
	j = j + 1
	'''if(G.has_node(arq[0][j])):
		j = j + 1
	elif(G.has_node(arq[1][j])):
		j = j + 1
	elif(G.has_node(arq[0][j])):
		G.add_node(arq[0][j])
		j = j + 1
	else:
		G.add_node(arq[1][j])
		j = j + 1
pos = pos=nx.fruchterman_reingold_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, arrows=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()'''
nx.write_gexf(G, 'grafo.gexf')
