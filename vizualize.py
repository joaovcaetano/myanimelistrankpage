#-*- coding: utf-8 -*-
import pandas as pd
import csv
import networkx as nx
import matplotlib.pyplot as plt
import re
#arquivo de leitura
arq = pd.read_csv('preprocessing.csv', sep = '\t', header = None)
i = 0
j = 0
base = 'pagerank.csv'
csv_modificado = open(base, "wb")
writer = csv.writer(csv_modificado, delimiter='\t')
base2 = 'indegree.csv'
csv_modificado2 = open(base2, "wb")
writer2 = csv.writer(csv_modificado2, delimiter='\t')
#declaracao do grafo
G = nx.DiGraph()
#inicio do codigo
while(j<len(arq[0])): #esse while cria os nós
	if(arq[2][j] != 0):
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

#nx.write_gexf(G, 'grafo.gexf')
print "iniciar qt degree"
degree = list(G.in_degree())
while i < len(degree):
	dados = list(degree[i])
	writer2.writerow(dados)
	i = i+1


print "iniciar page rank"

pr =  nx.pagerank(G)
i = 0
for i in pr:
	dados = []
	dados.append(i)
	dados.append(pr[i])
	writer.writerow(dados)
"""
while(i<len(pr)):
	dados = []
	dados.append(tabelaSaida[i][0])
	dados.append(tabelaSaida[i][1])
	dados.append(tabelaSaida[i][2])
	writer.writerow(dados)
	i = i+1
"""

"""#-*- coding: utf-8 -*-
import pandas as pd
import csv
from igraph import *
import matplotlib.pyplot as plt
import re
#arquivo de leitura
i = 0
j = 0
#declaracao do grafo
G = Graph()
#inicio do codigo
edge = []
weights = []
for i in range(len(arq[0])):
    for j in range(2):
        k =2
        edge.append(arq[j][i])
    weights.append(arq[k][i])
edges = [(i,j) for i,j in zip(edge[::2], edge[1::2])]
list1 = []
for i in range(len(edges)):
    list1.append((int(edges[i][0]), int(edges[i][1])))
G.add_vertices(40000)
G.add_edges(list1)
G.es['weight'] = weights
G.pagerank()
"""