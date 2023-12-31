import pandas as pd
import numpy as np
import limpfilt as lf
from limpfilt import *
import matplotlib.pyplot as plt
import seaborn as sns

#df = pd.read_csv('fa_casoshumanos_1994-2021.csv', sep = ';', encoding='ISO-8859-1')
#df.set_index('ID', inplace = True)

df = lf.carregar_dataframe('../fa_casoshumanos_1994-2021.csv')


lf.nan_cleaner(df)
lf.ftr_idades(df)
lf.rem_inv_dtis(df)
lf.rem_inv_obitos(df)
lf.rem_dupli(df)

#Dataframe com as colunas desejadas
ndf = lf.filtra_dados(df, colunas = ['SEXO','IDADE', 'ANO_IS', 'OBITO'], linhas=None, nome_csv=None)

# Mostra a quantidade de mortes entre o total de casos analisados
total = len(ndf['OBITO'])
mortes_count = ndf['OBITO'].value_counts()
porcent_obitos = (mortes_count["SIM"] / total) * 100

# Filtra o dataframe para obter apenas os casos com mortes 
mortes = ndf[ndf["OBITO"] == "SIM"]

# (vis1.png)
def tmortes_vis():
    """
    Cria a visualização da contagem de mortos do total de casos.
    Por esta análise é possível ver que na maior parte dos casos, 
    houve recuperação dentro do período de monitoramento.
    """
    plt.figure(figsize=(8, 6))
    ax = mortes_count.plot(kind="bar", color=["lightblue", "red"])
    plt.title("Contagem de Mortes")
    plt.xlabel("Número total de casos")
    plt.ylabel("")
    plt.xticks(rotation=0)

    # Adiciona a porcentagem ao rótulo das barras
    for i, count in enumerate(mortes_count):
        plt.text(i, count, f"{count} ({(count / total * 100):.2f}%)", ha="center", va="bottom")

    plt.show()


# (vis2.png)
def mtpor_ano():
    """
    Cria a visualização da contagem de mortos do total de casos ao longo do tempo.
    Tanto esta análise quanto a (vis3.png) apontam um surto de casos entre os anos 2016 e 2019, 
    que está em conforme com a realidade. Segundo a Biblioteca Virtual em Saúde:"Na última epidemia 
    registrada no Brasil, entre 2016 e 2019, cerca de 2,2 mil casos foram registrados e 759 pessoas morreram."
    Fonte: https://bvsms.saude.gov.br/pesquisa-avanca-no-desenvolvimento-de-terapia-para-febre-amarela/
    """
    
    mortes = ndf[ndf["OBITO"] == "SIM"]

    mortes_por_ano = mortes["ANO_IS"].value_counts().sort_index()

    plt.figure(figsize=(8, 6))
    ax = mortes_por_ano.plot(kind="bar", color="blue", width=0.8)
    plt.title("Total de mortes por ano")
    plt.xlabel("Ano")
    plt.ylabel("Número de mortes")
    ax.set_xticklabels(mortes_por_ano.index, rotation=45)
    plt.show()


# vis3.png)
def mtgenero_vis():
    """
    Cria a visualização da contagem de mortos por gênero ao longo do tempo.
    """

    # Agrupa por ano e gênero e conta o número de mortes 
    mortes_por_ano = mortes.groupby(["ANO_IS", "SEXO"]).size().unstack()

    mortes_por_ano.plot(kind="bar")
    plt.title("Mortes por gênero ao longo do tempo")
    plt.xlabel("Ano")
    plt.ylabel("Número de mortes")
    plt.legend(title="Gênero")
    plt.show()


# (vis4.png)
def mtidades_vis():
    intervalos_idade = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Cria coluna com os intervalos de idade
    mortes.loc[:, 'INT_I'] = pd.cut(mortes['IDADE'].astype(int), bins=intervalos_idade, right=False)

    # Cria uma matriz
    heatmap_data = mortes.pivot_table(index='INT_I', columns='ANO_IS', values='OBITO', aggfunc='count')

    plt.figure(figsize=(12,6))
    sns.heatmap(heatmap_data, cmap="YlOrRd", annot=True, fmt='g', linewidths=.5, cbar_kws={'label': 'Número de mortos'})
    plt.title("Quantidade de mortos ao longo do tempo")
    plt.xlabel("Ano")
    plt.ylabel("Idade")
    plt.show()

