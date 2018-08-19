# MyAnimeRanking!
# MyAnimeRanking é um novo sistema de rankeamento com base no site MyAnimeList.



# Arquivos

Dentre os arquivos utilizados temos:

	 - Anime.csv = Base do MyAnimeList contendo informações dos animes, como nome, nota geral, gênero, id.
	 - Basemenor.csv = Contém a nota dada pelo usuário para os animes vistos pelos mesmos.

# Scripts
Todos os algoritmos foram escritos em Python, dentre eles temos:

	 - preparaBase.py = gera a base separada por gênero para criar o sistema de rankeamento, para executar temos o seguinte comando: python preparaBase.py Genero, exemplo "python preparaBase.py Action".
	 - teste.py = responsável pela criação do novo ranking a partir da base gerada anteriormente.
