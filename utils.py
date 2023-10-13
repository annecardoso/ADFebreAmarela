import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

def carregar_dataframes():
    """
    Carrega DataFrames a partir de arquivos CSV e GeoJSON.

    Returns
    -------
    Tuple
        Um par de DataFrames contendo dados de óbitos e informações geoespaciais dos estados.
    """
    df = pd.read_csv('Dados/fa_casoshumanos_1994-2021.csv', sep=';', encoding='ISO-8859-1')
    states = gpd.read_file('Dados/br_states.json')
    return df, states

def obitos_por_uf(df, states):
    """
    Calcula o número de óbitos por unidade federativa e mescla com dados geoespaciais.

    Parameters
    ----------
    df : DataFrame
        DataFrame com informações de óbitos.
    states : GeoDataFrame
        GeoDataFrame com geometrias de estados.

    Returns
    -------
    GeoDataFrame
        Um GeoDataFrame que combina os dados de óbitos e informações geoespaciais.
    """
    df['OBITO'] = df['OBITO'].apply(lambda x: 1 if x=='SIM' else 0)
    obitos_por_uf = df[['UF_LPI', 'OBITO']].groupby(['UF_LPI']).sum()

    obitos_por_uf = obitos_por_uf.reset_index()
    obitos_por_uf = obitos_por_uf.rename(columns={'UF_LPI': 'PK_sigla'})
    gdf_obitos_uf = states.merge(obitos_por_uf, on='PK_sigla', how='left')
    gdf_obitos_uf = gdf_obitos_uf.fillna(0)

    return gdf_obitos_uf

def plot_obitos_uf(gdf_obitos_uf):
    """
    Gera um mapa de calor de óbitos por unidade federativa.

    Parameters
    ----------
    gdf_obitos_uf : GeoDataFrame
        GeoDataFrame contendo dados de óbitos por unidade federativa.
    """
    plot_ax = gdf_obitos_uf.plot(column = 'OBITO', legend=True, cmap='Reds')
    plot_ax.set_title('Óbitos por Unidade Federativa')
    plot_ax.set_axis_off()
    plt.show()

if __name__ == '__main__':
    df, states = carregar_dataframes()
    gdf_obitos_uf = obitos_por_uf(df, states)
    plot_obitos_uf(gdf_obitos_uf)

