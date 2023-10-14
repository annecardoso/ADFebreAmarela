import utils
import vizualizacao as viz
import matplotlib.pyplot as plt

# Carregamento das bases de dados
df, states = utils.carregar_dataframes()

# PERGUNTA 1-a): óbtios por estado
gdf_obitos_uf = utils.obitos_por_uf(df, states)

plt.figure(1)
grafico_1_a = viz.plot_mapa_uf(gdf_obitos_uf)
viz.definir_rotulos('Óbitos por Unidade Federativa',
                    '','')  # É definido o título do gráfico
grafico_1_a.set_axis_off()  # Os eixos do gráfico são removidos


plt.show() # Plota todas as figuras preestabelecidas