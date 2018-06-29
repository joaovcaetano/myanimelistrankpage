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

print "Verifica arestas invertendo sinal"
for edge in G.edges(data = 'weight'):
	if(edge[2] < 0):
		no1 = edge[0]
		no2 = edge[1]
		peso = abs(edge[2])
		G.remove_edge(*edge[:2])
		G.add_weighted_edges_from([(no2,no1,(peso))])

print "iniciar qt degree"
degree = list(G.in_degree())
while i < len(degree):
	dados = list(degree[i])
	writer2.writerow(dados)
	i = i+1
csv_modificado2.close()

print "iniciar page rank"

pr =  nx.pagerank(G)
i = 0
for i in pr:
	dados = []
	dados.append(i)
	dados.append(pr[i])
	writer.writerow(dados)
'''
print "grafo montado"
tabelaSaida = list(G.edges(data='weight'))
i = 0
while(i < len(tabelaSaida)):
	if handler.SIGINT == True:
		handler.status.append(i)
		print "to aqui montando grafo", handler.status
		print "e vai ate aqui", len(tabelaSaida)
		handler.status = []
		handler.SIGINT = False
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
'''
'''pos = pos=nx.fruchterman_reingold_layout(G)
plt.axis('auto')
nx.draw_networkx_nodes(G, pos,node_size=20)
nx.draw_networkx_labels(G, pos,alpha=0.4)
nx.draw_networkx_edges(G, pos, arrows=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()'''
