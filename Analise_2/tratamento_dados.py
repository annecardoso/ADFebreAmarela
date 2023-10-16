import pandas as pd
import limpfilt as lf
from pathlib import Path

def carregar_dataframes() -> pd.DataFrame:
    """
    Carrega um DataFrame a partir de um arquivo CSV.

    Retorno
    -------
    pd.DataFrame
        O DataFrame carregado com os dados ou None se houver um erro.
    """
    try:
        # Obtém o caminho para o arquivo com os dados da Febre Amarela
        raiz_do_projeto = str(Path(__file__).parent.parent)
        caminho_arquivo_FA = raiz_do_projeto + '/Dados/fa_casoshumanos_1994-2021.csv'

        # Tenta carregar um DataFrame a partir de um arquivo CSV
        df = pd.read_csv(caminho_arquivo_FA, sep=';', encoding='ISO-8859-1')
        return df
    except FileNotFoundError as e:
        # Trata exceção se o arquivo CSV não for encontrado
        print(f"Erro ao carregar o arquivo CSV: {e}")
        return None


def limpar_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza uma série de operações para limpar o DataFrame.

    Parâmetros
    ----------
    df : pd.DataFrame
        O DataFrame a ser limpo.

    Retorno
    -------
    pd.DataFrame
        O DataFrame limpo após as operações.
    """
    lf.nan_cleaner(df)
    lf.rem_inv_dtis(df)
    lf.ftr_idades(df)
    lf.rem_inv_obitos(df)
    df_limpo = lf.rem_dupli(df)
    return df_limpo

def organizar_df_datas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Faz um tratamento no DataFrame para que tenha apenas as informações de datas, óbitos e infecções.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame contendo as informações de datas e óbitos.

    Retorno
    -------
    pd.DataFrame
        Um novo DataFrame com as datas no formato desejado e a contagem de óbitos e infectados.
    """
    try:
        # Para evitar erro, criamos uma cópia do DataFrame recebido
        #df = df.copy()

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

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame contendo informações de datas, infecções e mortes.

    Retorno
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

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame contendo informações de datas, infecções e óbitos.

    Retorno
    -------
    pd.DataFrame
        Um novo DataFrame com a contagem de óbitos e infecções em cada mês.
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

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame agrupado por ano contendo informações de óbitos e infectados.

    Retorno
    -------
    pd.DataFrame
        Um novo DataFrame com uma relação de letalidade por ano.
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
