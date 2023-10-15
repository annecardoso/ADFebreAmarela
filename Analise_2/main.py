import pandas as pd

import Analise_2.tratamento_dados as td
import Analise_2.vizualizacao as viz

# Carregamento da bases de dados sobre febre amarela
df = td.carregar_dataframes()

# Mannipula o dataframe mantendo as informações pertinentes à questão
df_datas = td.organizar_df_datas(df)

# PERGUNTA 2-a): Qual a relação entre os anos e a quantidade de infecções e ou mortes?
ocorrencias_por_ano = td.organizar_df_ano(df_datas)
viz.plotar_ocorrencias_ano(ocorrencias_por_ano)

# PERGUNTA 2-b) No geral, há algum mês do ano com mais infecções?
df_meses = td.organizar_df_mes(df_datas)
viz.plotar_mortes_por_mes(df_meses)

# PERGUNTA 2-c) Há alguma relação entre a letalidade da doença e o passar do tempo?
df_letalidade = td.organizar_df_letalidade(ocorrencias_por_ano)
viz.plotar_letalidade(df_letalidade)
