import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

def carregar_dataframes() -> tuple:
    """
    Esta função carrega DataFrames a partir de arquivos CSV e GeoJSON.

    Retorno
    -------
    Tuple
        Um par de DataFrames contendo dados de óbitos e informações geoespaciais dos estados.
        
    >>> df, states = carregar_dataframes()
    >>> isinstance(df, pd.DataFrame)
    True
    >>> isinstance(states, gpd.GeoDataFrame)
    True
    """   
    try:
        # Tenta carregar um DataFrame a partir de um arquivo CSV
        df = pd.read_csv('Dados/fa_casoshumanos_1994-2021.csv', sep=';', encoding='ISO-8859-1')
        
    except FileNotFoundError as e:
        # Trata exceção se o arquivo CSV não for encontrado
        print(f"Erro ao carregar o arquivo CSV: {e}")
        df = None
        
    try:
        # Tenta carregar um GeoDataFrame a partir de um arquivo GeoJSON    
        states = gpd.read_file('Dados/br_states.json')
        
    except FileNotFoundError as e:
        # Trata exceção se o arquivo GeoJSON não for encontrado
        print(f"Erro ao carregar o arquivo GeoJSON: {e}")
        states = None
    
    return df, states

def filtragem_populacao(states_input: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Esta função faz uma cópia do GeoDataFrame de estados e atualiza a população total de estados específicos com base no Censo IBGE 2010.

    Parâmetros
    ----------
    states_input : GeoDataFrame
        GeoDataFrame contendo as geometrias de estados.

    Retorno
    -------
    GeoDataFrame
        Um novo GeoDataFrame com as populações de estados específicos atualizadas.

    >>> from geopandas import GeoDataFrame
    >>> import pandas as pd
    >>> data = {'SIGLA': ['SP', 'RJ', 'MG', 'PR'], 'Total': [0, 0, 0, 0]}
    >>> states_input = GeoDataFrame(pd.DataFrame(data))
    >>> states = filtragem_populacao(states_input)
    >>> isinstance(states, gpd.GeoDataFrame)
    True
    >>> states[states['SIGLA'] == 'SP']['Total'].values[0]
    37035456
    >>> states[states['SIGLA'] == 'PR']['Total'].values[0]
    9564643
    """
    try:
        states = states_input.copy()
        
        # Altera a população total de estados específicos com base no Censo IBGE 2010
        states.loc[states.SIGLA == 'SP', 'Total'] = 37035456
        states.loc[states.SIGLA == 'PR', 'Total'] = 9564643   
        return states

    except Exception as e:
        # Trata exceção se ocorrer um erro inesperado durante a filtragem
        print(f"Erro durante a filtragem de população: {e}")
        return None

def obitos_por_uf(df: pd.DataFrame, states: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Esta função calcula o número de óbitos por unidade federativa e mescla com dados geoespaciais.

    Parâmetros
    ----------
    df : DataFrame
        DataFrame com informações de óbitos.
    states : GeoDataFrame
        GeoDataFrame com geometrias de estados.

    Retorno
    -------
    GeoDataFrame
        Um GeoDataFrame que combina os dados de óbitos e informações geoespaciais.
        
    >>> df, states = carregar_dataframes()
    >>> gdf_obitos_uf = obitos_por_uf(df, states)
    >>> isinstance(gdf_obitos_uf, gpd.GeoDataFrame)
    True
    """   
    if df is None or states is None:
        # Verifica se os DataFrames foram carregados corretamente
        print("Os DataFrames não foram carregados corretamente. Não é possível realizar a análise.")
        return None
    
    try:
        # Converte a coluna 'OBITO' em valores binários (0 ou 1)
        df['OBITO'] = df['OBITO'].apply(lambda x: 1 if x=='SIM' else 0)
        
        # Calcula o número total de óbitos por unidade federativa 
        obitos_por_uf = df[['UF_LPI', 'OBITO']].groupby(['UF_LPI']).sum() 

        # Reorganiza o DataFrame para facilitar a mesclagem
        obitos_por_uf = obitos_por_uf.reset_index()
        obitos_por_uf = obitos_por_uf.rename(columns={'UF_LPI': 'PK_sigla'})
        
        # Mescla os dados de óbitos com as informações geoespaciais
        gdf_obitos_uf = states.merge(obitos_por_uf, on='PK_sigla', how='left') # Os dados das unidades federativas (states) são mesclados com os dados de óbitos (obitos_por_uf) com base na coluna ’PK_sigla’
        gdf_obitos_uf = gdf_obitos_uf.fillna(0) # Preenche unidades federativas sem dados de ́obitos com 0
        
        return gdf_obitos_uf
    
    except Exception as e:
        # Trata exceção se ocorrer um erro inesperado durante a análise de dados
        print(f"Erro durante a análise de dados: {e}")
        return None

def obitos_rel_por_uf(df: pd.DataFrame, states: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Esta função calcula a taxa de óbitos por 100.000 habitantes em cada unidade federativa, mesclando os dados com informações geoespaciais.

    Parâmetros
    ----------
    df : DataFrame
        DataFrame com informações de óbitos.
    states : GeoDataFrame
        GeoDataFrame com geometrias de estados.

    Retorno
    -------
    GeoDataFrame
        Um GeoDataFrame que combina os dados de óbitos relativos e informações geoespaciais.
    """
    if df is None or states is None:
        # Verifica se os DataFrames foram carregados corretamente
        print("Os DataFrames não foram carregados corretamente. Não é possível realizar a análise.")
        return None

    try:
        # Calcula o número total de óbitos por unidade federativa 
        obitos_por_uf = df[['UF_LPI', 'OBITO']].groupby(['UF_LPI']).sum()

        # Reorganiza o DataFrame para facilitar a mesclagem
        obitos_por_uf = obitos_por_uf.reset_index()
        obitos_por_uf = obitos_por_uf.rename(columns={'UF_LPI': 'PK_sigla'})

        # Mescla os dados de óbitos com as informações geoespaciais
        gdf_obitos_rel_uf = states.merge(obitos_por_uf, on='PK_sigla', how='left')
        gdf_obitos_rel_uf = gdf_obitos_rel_uf.fillna(0)

        # Calcula a taxa de óbitos por 100.000 habitantes
        gdf_obitos_rel_uf['OBITO_REL'] = 100000 * gdf_obitos_rel_uf['OBITO'] / gdf_obitos_rel_uf['Total']

        return gdf_obitos_rel_uf

    except Exception as e:
        # Trata exceção se ocorrer um erro inesperado durante a análise de dados
        print(f"Erro durante a análise de dados: {e}")
        return None

def infec_por_uf(df: pd.DataFrame, states: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Esta função calcula o número de infecções por unidade federativa, mesclando os dados com informações geoespaciais.

    Parâmetros
    ----------
    df : DataFrame
        DataFrame com informações de óbitos.
    states : GeoDataFrame
        GeoDataFrame com geometrias de estados.

    Retorno
    -------
    GeoDataFrame
        Um GeoDataFrame que combina os dados de infecções e informações geoespaciais.

    """
    if df is None or states is None:
        # Verifica se os DataFrames foram carregados corretamente
        print("Os DataFrames não foram carregados corretamente. Não é possível realizar a análise.")
        return None

    try:
        # Calcula o número total de infecções por unidade federativa 
        infec_por_uf = df[['UF_LPI', 'OBITO']].groupby(['UF_LPI']).count()

        # Reorganiza o DataFrame para facilitar a mesclagem
        infec_por_uf = infec_por_uf.reset_index()
        infec_por_uf = infec_por_uf.rename(columns ={'UF_LPI': 'PK_sigla'})

        # Mescla os dados de infecções com as informações geoespaciais
        gdf_infec_uf = states.merge(infec_por_uf, on='PK_sigla', how='left')
        gdf_infec_uf = gdf_infec_uf.fillna(0)

        return gdf_infec_uf

    except Exception as e:
        # Trata exceção se ocorrer um erro inesperado durante a análise de dados
        print(f"Erro durante a análise de dados: {e}")
        return None

def infec_rel_por_uf(df: pd.DataFrame, states: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Esta função calcula a taxa de infecção por cada 100.000 habitantes por unidade federativa, mesclando os dados com informações geoespaciais.

    Parâmetros
    ----------
    df : DataFrame
        DataFrame com informações de óbitos.
    states : GeoDataFrame
        GeoDataFrame com geometrias de estados.

    Retorno
    -------
    GeoDataFrame
        Um GeoDataFrame que combina os dados da taxa de infecção e informações geoespaciais.

    """
    if df is None or states is None:
        # Verifica se os DataFrames foram carregados corretamente
        print("Os DataFrames não foram carregados corretamente. Não é possível realizar a análise.")
        return None

    try:
        # Calcula o número total de infecções por unidade federativa 
        infec_rel_por_uf = df[['UF_LPI', 'OBITO']].groupby(['UF_LPI']).count()

        # Reorganiza o DataFrame para facilitar a mesclagem
        infec_rel_por_uf = infec_rel_por_uf.reset_index()
        infec_rel_por_uf = infec_rel_por_uf.rename(columns ={'UF_LPI': 'PK_sigla'})

        # Mescla os dados da taxa de infecção com as informações geoespaciais
        gdf_infec_rel_uf = states.merge(infec_rel_por_uf, on='PK_sigla', how='left')
        gdf_infec_rel_uf = gdf_infec_rel_uf.fillna(0)

        # Calcula a taxa de infecção por cada 100.000 habitantes
        gdf_infec_rel_uf['INFEC_REL'] = 100000 * gdf_infec_rel_uf['OBITO'] / gdf_infec_rel_uf['Total']

        return gdf_infec_rel_uf

    except Exception as e:
        # Trata exceção se ocorrer um erro inesperado durante a análise de dados
        print(f"Erro durante a análise de dados: {e}")
        return None

def plot_obitos_uf(gdf_obitos_uf: gpd.GeoDataFrame) -> None:
    """
    Esta função gera um mapa de calor de óbitos por unidade federativa.

    Parâmetros
    ----------
    gdf_obitos_uf : GeoDataFrame
        GeoDataFrame contendo dados de óbitos por unidade federativa.
    """
       
    if gdf_obitos_uf is None:
        # Verifica se o GeoDataFrame foi gerado corretamente
        print("O GeoDataFrame não foi gerado corretamente. Não é possível gerar o mapa.")
        return

    try:
        # Plota um mapa de calor com base nos dados de óbitos
        plot_ax = gdf_obitos_uf.plot(column = 'OBITO', legend=True, cmap='Reds') # Um gráfico geoespacial é criado usando a coluna ’OBITO’ do DataFrame 
        plot_ax.set_title('Óbitos por Unidade Federativa') # É definido o título do mapa
        plot_ax.set_axis_off() # Os eixos do gráfico são removidos
        plt.show()
    
    except Exception as e:
        # Trata exceção se ocorrer um erro inesperado durante a geração do mapa
        print(f"Erro durante a geração do mapa: {e}")

def plot_obitos_rel_uf(gdf_obitos_rel_uf: gpd.GeoDataFrame) -> None:
    """
    Esta função gera um mapa de calor representando a taxa de óbitos por cada 100.000 habitantes por unidade federativa.

    Parâmetros
    ----------
    gdf_obitos_rel_uf : GeoDataFrame
        GeoDataFrame contendo dados da taxa de óbitos por cada 100.000 habitantes por unidade federativa.

    Retorno
    -------
    None
    """
    if gdf_obitos_rel_uf is None:
        # Verifica se o GeoDataFrame foi gerado corretamente
        print("O GeoDataFrame não foi gerado corretamente. Não é possível gerar o mapa.")
        return

    try:
        # Plota um mapa de calor com base na taxa de óbitos por cada 100.000 habitantes
        plot_ax = gdf_obitos_rel_uf.plot(column='OBITO_REL', legend=True, cmap='Reds')
        plot_ax.set_title('Óbitos por cada 100.000 habitantes por Unidade Federativa')
        plot_ax.set_axis_off()
        plt.show()
    
    except Exception as e:
        # Trata exceção se ocorrer um erro inesperado durante a geração do mapa
        print(f"Erro durante a geração do mapa: {e}")

def plot_infec_uf(gdf_infec_rel_uf: gpd.GeoDataFrame) -> None:
    """
    Gera um mapa de calor de infecções por unidade federativa.

    Esta função gera um mapa de calor representando o número de infecções por unidade federativa.

    Parâmetros
    ----------
    gdf_infec_rel_uf : GeoDataFrame
        GeoDataFrame contendo dados do número de infecções por unidade federativa.

    Retorno
    -------
    None

    """
    if gdf_infec_rel_uf is None:
        # Verifica se o GeoDataFrame foi gerado corretamente
        print("O GeoDataFrame não foi gerado corretamente. Não é possível gerar o mapa.")
        return

    try:
        # Plota um mapa de calor com base no número de infecções
        plot_ax = gdf_infec_rel_uf.plot(column='OBITO', legend=True, cmap='Reds')
        plot_ax.set_title('Infecções por Unidade Federativa')
        plot_ax.set_axis_off()
        plt.show()
    
    except Exception as e:
        # Trata exceção se ocorrer um erro inesperado durante a geração do mapa
        print(f"Erro durante a geração do mapa: {e}")

def plot_infec_rel_uf(gdf_infec_rel_uf: gpd.GeoDataFrame) -> None:
    """
    Esta função gera um mapa de calor representando o número de infecções por cada 100.000 habitantes por unidade federativa.

    Parâmetros
    ----------
    gdf_infec_rel_uf : GeoDataFrame
        GeoDataFrame contendo dados do número de infecções por cada 100.000 habitantes por unidade federativa.

    Retorno
    -------
    None

    """
    if gdf_infec_rel_uf is None:
        # Verifica se o GeoDataFrame foi gerado corretamente
        print("O GeoDataFrame não foi gerado corretamente. Não é possível gerar o mapa.")
        return

    try:
        # Plota um mapa de calor com base no número de infecções por cada 100.000 habitantes
        plot_ax = gdf_infec_rel_uf.plot(column='INFEC_REL', legend=True, cmap='Reds')
        plot_ax.set_title('Infecções por cada 100.000 habitantes por Unidade Federativa')
        plot_ax.set_axis_off()
        plt.show()
    
    except Exception as e:
        # Trata exceção se ocorrer um erro inesperado durante a geração do mapa
        print(f"Erro durante a geração do mapa: {e}")
