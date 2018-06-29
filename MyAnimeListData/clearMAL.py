import pandas as pd
import csv

arquivo = pd.read_csv('anime.csv',delimiter=",",header=None)
base_saida = 'malsaida.csv'
csv_modificado = open(base_saida, "wb")
writer = csv.writer(csv_modificado, delimiter='\t')

i = 1
j = 1
while(i<len(arquivo[0])):
	texto = str(arquivo[2][i])
	texto = texto.split(", ")
	if("Shounen" in texto):
		writer.writerow((arquivo[0][i],arquivo[5][i]))
	i = i+1