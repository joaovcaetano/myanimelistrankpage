import pandas as pd
import csv

arquivo = pd.read_csv('anime.csv',delimiter=",",header=None)
base_saida = 'malsaida.csv'
csv_modificado = open(base_saida, "wb")
writer = csv.writer(csv_modificado, delimiter='\t')

i = 1
j = 1
while(i<len(arquivo[0])):
	if int(arquivo[0][i]) < 10000:
		writer.writerow((arquivo[5][i],arquivo[0][i]))
		j = j+1
	i = i+1