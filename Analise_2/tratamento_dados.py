import pandas as pd
import limpfilt as lf

def organizar_df_datas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Faz um tratamento no DataFrame para que tenha apenas as informações de datas, óbitos e infecções.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contendo as informações de datas e óbitos.

    Returns
    -------
    pd.DataFrame
        Um novo DataFrame com as datas no formato desejado e a contagem de óbitos e infectados.

    Exemplo
    -------
    >>> dados = {'ANO_IS': [2019, 2020, 2021], 'MES_IS': [1.0, 1.0, 4.0], 'OBITO': ['SIM', 'NÃO', 'IGN']}
    >>> df = pd.DataFrame(dados)
    >>> saida = organizar_df_datas(df)
    >>> isinstance(saida, pd.DataFrame)
    True
    >>> set(saida['ANO_IS'].unique()) == {2019,2020,2021}
    True
    >>> set(saida['OBITO'].unique()) == {0,1}
    True
    >>> isinstance(saida['INFECTADOS'],pd.Series)
    True
    """
    try:
        # Converte a coluna 'OBITO' em valores binários (0 ou 1)
        df['OBITO'] = df['OBITO'].apply(lambda x: 1 if x == 'SIM' else 0)


        df_datas = df[['ANO_IS', 'MES_IS', 'OBITO']]
        df_datas.insert(2, 'INFECTADOS', 1, True)  # Adiciona uma coluna para guardar a quantidade de infectados

        df_datas = df_datas.groupby(['ANO_IS', 'MES_IS']).sum()  # Agrupa o DataFrame por ano e mês
        df_datas = df_datas.reset_index()
        return df_datas
    except KeyError as e:
        # Trata exceção se as colunas necessárias não estiverem presentes no DataFrame
        print(f"Erro ao organizar DataFrame: {e}")
        return None


def organizar_df_ano(df: pd.DataFrame) -> pd.DataFrame:
    """
    Organiza um DataFrame relacionando a cada ano uma quantidade de casos e mortes por febre amarela.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contendo informações de datas, infecções e mortes.

    Returns
    -------
    pd.DataFrame
        Um novo DataFrame com o número de infectados e mortos por ano.
    """
    try:
        df = lf.remover_coluna(df, 'MES_IS')
        df = df.groupby(['ANO_IS']).sum()
        df = df.reset_index()
        return df
    except KeyError as e:
        # Trata exceção se as colunas necessárias não estiverem presentes no DataFrame
        print(f"Erro ao organizar DataFrame: {e}")
        return None


def organizar_df_mes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Organiza o DataFrame para facilitar uma análise específica, reduzindo os dados ao total de infecções e óbitos em relação aos meses do ano.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contendo informações de datas, infecções e óbitos.

    Returns
    -------
    pd.DataFrame
        Um novo DataFrame com a contagem de óbitos e infecções em cada mês.

    Exemplo
    -------
    >>> dados = {'ANO_IS': [2019, 2020, 2021], 'MES_IS': [1.0, 1.0, 4.0], 'OBITO': [1, 1, 0], 'INFECTADOS':[1, 1, 1]}
    >>> df = pd.DataFrame(dados)
    >>> saida = organizar_df_mes(df)
    >>> meses = saida['MES_IS'].unique()
    >>> set(meses) == {'abril','janeiro'}
    True
    >>> obitos = saida['OBITO']
    >>> obitos[0] == 2
    True
    >>> saida['INFECTADOS'][1] == 1
    True
    """
    try:
        df = lf.remover_coluna(df, 'ANO_IS')
        df = df.groupby(['MES_IS']).sum()
        df = df.reset_index()

        # Dicionário que relaciona o número dos meses aos seus nomes
        meses = {1.0: 'janeiro', 2.0: 'fevereiro', 3.0: 'março', 4.0: 'abril', 5.0: 'maio', 6.0: 'junho',
                 7.0: 'julho', 8.0: 'agosto', 9.0: 'setembro', 10.0: 'outubro', 11.0: 'novembro', 12.0: 'dezembro'}
        # Altera a coluna MES_IS para conter os meses em texto
        df['MES_IS'] = df['MES_IS'].map(meses)

        return df
    except KeyError as e:
        # Trata exceção se as colunas necessárias não estiverem presentes no DataFrame
        print(f"Erro ao organizar DataFrame: {e}")
        return None


def organizar_df_letalidade(df: pd.DataFrame) -> pd.DataFrame:
    """
    Organiza o DataFrame para facilitar uma análise específica. Para isso,
    há a exclusão de colunas e adição de uma coluna referente à letalidade da doença.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame agrupado por ano contendo informações de óbitos e infectados.

    Returns
    -------
    pd.DataFrame
        Um novo DataFrame com uma relação de letalidade por ano.

    Exemplo
    -------
    >>> dados = {'ANO_IS': [2019, 2020, 2021], 'OBITO': [10, 3, 30], 'INFECTADOS': [20, 15, 50]}
    >>> df = pd.DataFrame(dados)
    >>> saida = organizar_df_letalidade(df)
    >>> letalidade = saida['LETALIDADE']
    >>> letalidade.iloc[0] == 0.5
    True
    >>> letalidade.iloc[1] == 0.2
    True
    >>> letalidade.iloc[2] == 0.6
    True
    """
    try:
        # Adição da coluna LETALIDADE
        df['LETALIDADE'] = df['OBITO'] / df['INFECTADOS']
        # Exclusão das colunas desnecessárias
        df = lf.remover_coluna(df, 'OBITO')
        return df
    except KeyError as e:
        # Trata exceção se as colunas necessárias não estiverem presentes no DataFrame
        print(f"Erro ao organizar DataFrame: {e}")
        return None
