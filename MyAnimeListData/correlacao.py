from scipy import stats
import pandas as pd
import csv
arq1 = pd.read_csv('normalizado.csv',sep= '\t', header = None)
arq2 = pd.read_csv('malsaida.csv', sep = '\t', header = None)
lista_page = []
lista_my_anime_data = []
lista_anime = []
j = 0
i = 0
#base = "corre.csv"
#csv_modificado = open(base, "wb")
#writer = csv.writer(csv_modificado, delimiter='\t')
lista = []
tabela = []
#k = 0

while (i< len(arq2[0]) and j<len(arq1[0])):
	if (int(arq2[1][i]) < int(arq1[0][j])):
		i = i + 1
	elif (int(arq2[1][i]) > int(arq1[0][j])):
		j = j + 1
	else:
		u0 = arq1[0][j]
		u1 = float(arq1[2][j])
		u2 = float(arq2[0][i])
		lista_anime.append(arq1[0][j])
		lista_page.append(float(arq1[2][j]))
		lista_my_anime_data.append(float(arq2[0][i]))
		#tabela.append([u0,u1,u2])
		#writer.writerow(tabela[k])
		#k = k + 1
		j = j+1
		i = i+1
df = stats.spearmanr(lista_page, lista_my_anime_data, nan_policy = 'omit')
print df
'''
def correlation_matrix(df):
    from matplotlib import pyplot as plt
    from matplotlib import cm as cm
    corr = pd.DataFrame()
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    cmap = cm.get_cmap('jet', 30)
    cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
    ax1.grid(True)
    plt.title('Abalone Feature Correlation')
    labels=lista_anime
    ax1.set_xticklabels(labels,fontsize=6)
    ax1.set_yticklabels(labels,fontsize=6)
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    fig.colorbar(cax, ticks=[.75,.8,.85,.90,.95,1])
    plt.show()

correlation_matrix(df)

'''