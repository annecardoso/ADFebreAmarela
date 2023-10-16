import pandas as pd
import geopandas as gpd
import utils

df, states = utils.carregar_dataframes()
states = utils.filtragem_populacao(states)

# Analisa os óbitos por unidade federativa
gdf_obitos_uf = utils.obitos_por_uf(df, states)
utils.plot_obitos_uf(gdf_obitos_uf)

# Analisa os óbitos de forma relativa (óbitos a cada 100.000 habitantes) por unidade federativa
gdf_obitos_rel_uf = utils.obitos_rel_por_uf(df, states)
utils.plot_obitos_rel_uf(gdf_obitos_rel_uf)

# Analisa as notificações de infecção por unidade federativa
gdf_infec_uf = utils.infec_por_uf(df, states)
utils.plot_infec_uf(gdf_infec_uf)

# Analisa as notificações de infecção de forma relativa (a cada 100.000 habitantes) por unidade federativa
gdf_infec_rel_uf = utils.infec_rel_por_uf(df, states)
utils.plot_infec_rel_uf(gdf_infec_rel_uf)
