import utils
import vizualizacao as viz
import matplotlib.pyplot as plt

# Carregamento das bases de dados
df, states = utils.carregar_dataframes()

# PERGUNTA X: óbtios por estado
gdf_obitos_uf = utils.obitos_por_uf(df, states)

plt.figure(1)
grafico_X_a = viz.plot_mapa_uf(gdf_obitos_uf)
grafico_X_a.set_title('Óbitos por Unidade Federativa')  # É definido o título do mapa
grafico_X_a.set_axis_off()  # Os eixos do gráfico são removidos


plt.show() # Plota todas as figuras preestabelecidas