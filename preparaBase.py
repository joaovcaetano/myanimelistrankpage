#-*- coding: utf-8 -*-
import pandas as pd
import csv
import sys
genero = sys.argv[1]

def geraGenero():
	arquivo = pd.read_csv('anime.csv',delimiter=",",header=None)
	base = "genero.csv"
	csv_modificado = open(base, "wb")
	writer = csv.writer(csv_modificado, delimiter = '\t')
	anime = []
	k = 1
	for i in range(0, len(arquivo[0])):
		texto = str(arquivo[2][i])
		texto = texto.split(", ")
		if genero in texto:
			writer.writerow((arquivo[0][i],arquivo[5][i]))
	csv_modificado.close()

def geraTodosUsuarios():
	arq = pd.read_csv('basemenor.csv', sep = ';', header = None)
	i = 0
	base = 'basefinal.csv'
	basemal = "genero.csv"
	mal = pd.read_csv(basemal, sep = '\t', header = None)
	csv_modificado = open(base, "wb")
	writer = csv.writer(csv_modificado, delimiter='\t')
	k = 0
	tabela = []
	fall = []
	for j in range(0,len(mal[0])):
		fall.append(int(mal[0][j]))
	while(i<len(arq[0])):
		if arq[1][i] in fall:
			u0 = arq[0][i]
			u1 = arq[1][i]
			u2 = arq[2][i]
			tabela.append([u0,u1,u2])
			writer.writerow(tabela[k])
			k = k+1
		i = i + 1


def separaUsuario():
	arq = pd.read_csv('basefinal.csv', sep = '\t', header = None)
	i = 0
	#c = 1000
	tabelaFinal = []
	tabela = []
	while(i<len(arq[0])):
		u0 = arq[0][i]
		base = "users/user"+str(u0)+".csv"
		csv_modificado = open(base, "wb")
		writer = csv.writer(csv_modificado, delimiter='\t')
		tabela = []
		j =0
		while(i<len(arq[0])):#esse while monta tabela
			if(arq[0][i] == u0):
				u1 = arq[1][i]
				u2 = arq[2][i]
				tabela.append([u0,u1,u2])
				writer.writerow(tabela[j])
				j = j+1
				i = i + 1
			else:
				break

geraGenero()
print "Gera Genero"
geraTodosUsuarios()
print "To separando usuários"
separaUsuario()