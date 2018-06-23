import pandas as pd
import csv

arquivo = pd.read_csv('anime.csv',delimiter=",",header=None)
base_saida = 'malranking.csv'
csv_modificado = open(base_saida, "wb")
writer = csv.writer(csv_modificado, delimiter='\t')
i = 1
while(i<len(arquivo[0])):
	writer.writerow(arquivo[0][i])
	i = i+1