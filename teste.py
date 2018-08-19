#-*- coding: utf-8 -*-
import pandas as pd
import csv
import networkx as nx
import matplotlib.pyplot as plt
import re
import signal
import time
import os
pasta = "users"
caminhos = [os.path.join(pasta,nome) for nome in os.listdir(pasta)]
arquivos = [ar for ar in caminhos if os.path.isfile(ar)]
print 'turubom'

class SIGINT_handler():
    def __init__(self):
        self.SIGINT = False
        self.status = []

    def signal_handler(self, signal, frame):
        self.SIGINT = True

handler = SIGINT_handler()
signal.signal(signal.SIGINT, handler.signal_handler)
def calculaPeso(tabela1):
	i = 0
	j = 1
	while(i<len(tabela1)):
		while(j<len(tabela1)):
			new_value_weight = tabela1[2][j] - tabela1[2][i]
			if(G.has_edge(tabela1[1][j],tabela1[1][i])):
				G.add_weighted_edges_from([(tabela1[1][j],tabela1[1][i],(G[tabela1[1][j]][tabela1[1][i]]['weight']+new_value_weight))])
				j = j + 1
			elif(G.has_edge(tabela1[1][i],tabela1[1][j])):
				G.add_weighted_edges_from([(tabela1[1][i],tabela1[1][j],(G[tabela1[1][i]][tabela1[1][j]]['weight']+new_value_weight))])
				j = j + 1
			else:
				G.add_weighted_edges_from([(tabela1[1][i],tabela1[1][j],(new_value_weight))])
				j = j + 1
		i = i + 1
		j = i+1
#indices
i = 0
cont = 0
j = 0
#declaracao do grafo
G = nx.DiGraph()
#arquivo de saida
base3 = 'preprocessing.csv'
csv_modificado3 = open(base3, "wb")
writer3 = csv.writer(csv_modificado3, delimiter='\t')
base = 'pagerank.csv'
csv_modificado = open(base, "wb")
writer = csv.writer(csv_modificado, delimiter='\t')
base2 = 'pagerank1.csv'
csv_modificado2 = open(base2, "wb")
writer2 = csv.writer(csv_modificado2, delimiter='\t')
contador = 0
#inicio do codigo
print "len users", len(arquivos)
for y in range(0,len(arquivos)):
	userAtual = arquivos[y]
	tabela1 = pd.read_csv(userAtual, sep = '\t', header = None)
	if handler.SIGINT == True:
		handler.status.append(y)
		print "montando a tabela do usuario", handler.status
		handler.status = []
		handler.SIGINT = False
	while(j<len(tabela1)):#esse while cria os nós
		if G.has_node(tabela1[1][j]):
			G.add_node(tabela1[1][j])
		j = j + 1
	calculaPeso(tabela1)
tabela1 = []
lista_aux = []
print "viram yamato", contador
print "Verifica arestas invertendo sinal"
print len(G.edges())
for edge in G.edges(data = 'weight'):
	if(edge[2] < 0):
		no1 = edge[0]
		no2 = edge[1]
		peso = abs(edge[2])
		'''peso_real = int(edge[2])
		if((int(no1) == 4773) or (int(no2) == 4773)):
			lista_aux.append([no1, no2, peso_real])'''
		G.remove_edge(*edge[:2])
		G.add_weighted_edges_from([(no2,no1,(peso))])
print "iniciar qt indegree"
#csv_modificado4 = open("yamato_takeru.csv", "wb")
#writer4 = csv.writer(csv_modificado4, delimiter='\t')
degree = list(G.in_degree())
outdegree = list(G.out_degree())

while i < len(degree):
	dados = list(degree[i])
	dados2 = list(outdegree[i])
	writer2.writerow((dados[0],dados[1], dados2[1]))
	i = i+1
'''for z in range(0,len(lista_aux)):
	writer4.writerow((lista_aux[z][0], lista_aux[z][1], lista_aux[z][2]))'''
csv_modificado2.close()
#csv_modificado4.close()

print "iniciar page rank"

pr =  nx.pagerank(G)
i = 0
for i in pr:
	dados = []
	dados.append(i)
	dados.append(pr[i])
	writer.writerow(dados)
'''pos = pos=nx.fruchterman_reingold_layout(G)
plt.axis('auto')
nx.draw_networkx_nodes(G, pos,node_size=20)
nx.draw_networkx_labels(G, pos,alpha=0.4)
nx.draw_networkx_edges(G, pos, arrows=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()'''
