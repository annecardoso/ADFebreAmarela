import tratamento_dados as td
import visualizacao as vis

# Carregamento da bases de dados sobre febre amarela
df = td.lf.carregar_dataframe('fa_casoshumanos_1994-2021.csv')

# Limpeza do dataframe
df = td.lf.limpar_dataframe(df)

# Mannipula o dataframe mantendo as informações pertinentes à questão
df_datas = td.organizar_df_datas(df)

# PERGUNTA 2-a): Qual a relação entre os anos e a quantidade de infecções e ou mortes?
ocorrencias_por_ano = td.organizar_df_ano(df_datas)
vis.plotar_ocorrencias_ano(ocorrencias_por_ano)

# PERGUNTA 2-b) No geral, há algum mês do ano com mais infecções?
ocorrencias_por_mes = td.organizar_df_mes(df_datas)
vis.plotar_mortes_por_mes(ocorrencias_por_mes)

# PERGUNTA 2-c) Há alguma relação entre a letalidade da doença e o passar do tempo?
letalidade_por_ano = td.organizar_df_letalidade(ocorrencias_por_ano)
vis.plotar_letalidade(letalidade_por_ano)