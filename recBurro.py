#-*- coding: utf-8 -*-
import pandas as pd
import csv
import sys
import os

userAtual = "users/user11359.csv"
arq = pd.read_csv(userAtual, sep = '\t', header = None)
#leitura do user em uma tabela
i = 0
count = 0
u0 = arq[0][i]
tabelaFinal = []
tabela = []
print "first while"
while(i<len(arq[0])):#esse while monta tabela
	u1 = arq[1][i]
	tabela.append([u1])
	i = i+1
i = 0
count = 0
arqAux = pd.read_csv("pagerank2.csv", sep = '\t', header = None)
while(i<len(arqAux[0])):#esse while monta tabela
	u2 = arqAux[0][i]
	if not (u2 in tabela): 
		print u2
		if count < 5:
			count = count +1
		else:
			break
	i = i+1