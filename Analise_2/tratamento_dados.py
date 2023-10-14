import pandas as pd
from pathlib import Path

def carregar_dataframes() -> None:
    """
    Carrega DataFrames a partir de arquivos CSV

    Parâmetros
    ----------
    None

    Retorno
    -------
    Tuple
        Um par de DataFrames contendo dados de óbitos e informações geoespaciais dos estados.
    """
    try:
        # Tenta carregar um DataFrame a partir de um arquivo CSV
        raiz_do_projeto = str(Path(__file__).parent.parent) # Caminho absoluto até a raiz do projeto
        caminho_arquivo_FA = raiz_do_projeto + '/Dados/fa_casoshumanos_1994-2021.csv'

        df = pd.read_csv(caminho_arquivo_FA, sep=';', encoding='ISO-8859-1')
        
    except FileNotFoundError as e:
        # Trata exceção se o arquivo CSV não for encontrado
        print(f"Erro ao carregar o arquivo CSV: {e}")
        df = None

    return df


def organizar_df_datas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Separa e transforma um DataFrame com informações de datas, óbitos e infecções.

    Parâmetros
    ----------
    df : pandas.DataFrame
        DataFrame contendo as informações de datas e óbitos.

    Returno
    -------
    pandas.DataFrame
        Um novo DataFrame com as datas no formato desejado e a contagem de óbitos e infectados.
    """
    # Converte a coluna 'OBITO' em valores binários (0 ou 1)
    df['OBITO'] = df['OBITO'].apply(lambda x: 1 if x == 'SIM' else 0)
    df_datas = df[['ANO_IS', 'MES_IS', 'OBITO']]  # Cria um novo DataFrame com as informações pertinentes
    df_datas.insert(2, 'INFECTADOS', 1, True)  # Adiciona uma coluna para guardar a quantidade de infectados
    df_datas = df_datas.groupby(['ANO_IS', 'MES_IS']).sum()  # Agrupa o DataFrame por ano e mês
    df_datas = df_datas.reset_index()  # Como o DataFrame é reduzido, convém redefinir os índices

    return df_datas


def organizar_df_ano(df:pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=['MES_IS'])
    df = df.groupby(['ANO_IS']).sum()
    df = df.reset_index()

    return df

def organizar_df_mes(df:pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=['ANO_IS'])
    df = df.groupby(['MES_IS']).sum()
    df = df.reset_index()

    # Altera a coluna MES_IS para conter os meses em texto
    meses = {1.0: 'janeiro', 2.0: 'fevereiro', 3.0: 'março', 4.0: 'abril', 5.0: 'maio', 6.0: 'junho',
             7.0: 'julho', 8.0: 'agosto', 9.0: 'setembro', 10.0: 'outubro', 11.0: 'novembro', 12.0: 'dezembro'}

    df['MES_IS'] = df['MES_IS'].map(meses)

    return df

def organizar_df_letalidade(df:pd.DataFrame) -> pd.DataFrame:
    df['LETALIDADE'] = df['OBITO'] / df['INFECTADOS']
    df = df.drop(columns=['INFECTADOS'])
    df = df.drop(columns=['OBITO'])
    return df
