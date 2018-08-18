#-*- coding: utf-8 -*-
import pandas as pd
import csv
import networkx as nx
import matplotlib.pyplot as plt
arq = pd.read_csv('basefinal.csv', sep = '\t', header = None)
i = 0
#c = 1000
tabelaFinal = []
tabela = []
flag2 = 0
flag1 = 0
for j in range(0, len(arq[0])):
	numero = int(arq[1][i])
	tabela.append(numero)
while(i<len(arq[0])):
	u0 = 4773
	u1 = 9376
	if u0 in tabela:
		flag1 = flag1 + 1
	elif u1 in tabela:
		flag2 = flag2 + 1
			
print flag1, flag2