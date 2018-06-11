from igraph import *

# Here we have 5 edges
a = [('1', '177', 1.0), ('1', '54', 1.0), ('1', '61', 2.0), 
     ('1', '86', 2.0), ('10', '100', 38.0)]    

edge = []
weights = []
# the loop for i is in range(5) because you have 5 edges
for i in range(5):
    for j in range(2):
        k =2
        edge.append(a[i][j])
    weights.append(a[i][k])

edges = [(i,j) for i,j in zip(edge[::2], edge[1::2])]

list1 = []
for i in range(len(edges)):
    list1.append((int(edges[i][0]), int(edges[i][1])))

g= Graph()
g.add_vertices(178)
g.add_edges(list1)
g.es['weight'] = weights

"""#-*- coding: utf-8 -*-
import pandas as pd
import csv
from igraph import *
import matplotlib.pyplot as plt
import re
#arquivo de leitura
arq = pd.read_csv('win.csv', sep = '\t', header = None)
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