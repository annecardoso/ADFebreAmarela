import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Dados/fa_casoshumanos_1994-2021.csv', sep=';', encoding='ISO-8859-1')

states = gpd.read_file('Dados/br_states.json')

df['OBITO'] = df['OBITO'].apply(lambda x: 1 if x=='SIM' else 0)
obitos_por_uf = df[['UF_LPI', 'OBITO']].groupby(['UF_LPI']).sum()

obitos_por_uf = obitos_por_uf.reset_index()
obitos_por_uf = obitos_por_uf.rename(columns={'UF_LPI': 'PK_sigla'})
gdf_obitos_uf = states.merge(obitos_por_uf, on='PK_sigla', how='left')
gdf_obitos_uf = gdf_obitos_uf.fillna(0)

plot_ax = gdf_obitos_uf.plot(column = 'OBITO', legend=True, cmap='Reds')
plot_ax.set_title('Óbitos por Unidade Federativa')
plot_ax.set_axis_off()
plt.show()


