import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path


def carregar_dataframe(arquivo:str) -> pd.DataFrame:
    """
    Carrega um DataFrame a partir de um arquivo CSV.

    Parâmetros
    ----------
    str
        Uma string com o nome do arquivo da pasta Dados a ser carregado como DataFrame

    Retorno
    -------
    pd.DataFrame
        O DataFrame carregado com os dados ou None se houver um erro.
    """
    try:
        # Obtém o caminho para o arquivo com os dados da Febre Amarela
        raiz_do_projeto = str(Path(__file__).parent)
        caminho_arquivo = raiz_do_projeto + '/Dados/' + arquivo

        # Obtém a extensão do arquivo
        extensao = Path(caminho_arquivo).suffix

        # Tenta carregar um DataFrame a partir de um arquivo
        if extensao == '.csv':
            df = pd.read_csv(caminho_arquivo, sep=';', encoding='ISO-8859-1')
        else:
            raise ValueError

        df.set_index('ID', inplace=True)
        return df
    except FileNotFoundError as excp:
        # Trata exceção se o arquivo CSV não for encontrado
        print(f"Erro ao carregar o arquivo: {excp}")
        return None
    except ValueError as excp:
        print(f"Erro {excp}. O arquivo não é de um tipo suportado, ele deve ser um CSV.")
    except Exception as excp:
        print(f"Erro ao carregar o dataframe: {excp}")



def nan_cleaner(df):
    """
    Cria um dataframe apenas com as linhas que possuem valores NaN 
    e modifica o dataframe original, retirando-as.

    Parâmetros
    ----------
    df : pd.DataFrame
    Retorno
    -------
    pd.DataFrame
        Dataframe destacado com linhas NaN.
    Exemplos
    --------
    >>> df1 = pd.df(np.array([[1, 2, 3], [4, pd.NA, 6], [7, 8, 9]]),
    ...                    columns=['a', 'b', 'c'])
    >>> nan_cleaner(df1)
       a     b  c
    1  4  <NA>  6
    """
    bolean_df = df.isna()
    bolean_sum = bolean_df.sum(axis=1) > 0
    na_df = df[bolean_sum]
    df.dropna(inplace=True)
    return na_df


def rem_dupli(df):
    """
    Remove linhas duplicadas.

    Parâmetros
    ----------
    df : pd.DataFrame
    Retorno
    -------
    pd.DataFrame 
        Dataframe atualizado.
    Exemplos
    --------
    >>> df2 = pd.df(np.array([[1, 2, 3], [4, 5, 6], [4, 5, 6], [7, 8, 9], [1, 2, 3]]),
    ...                    columns=['a', 'b', 'c'])
    >>> rem_dupli(df2)
       a  b  c
    0  1  2  3
    1  4  5  6
    3  7  8  9
    """
    df.drop_duplicates(inplace=True)
    return df


def ftr_dt_is(data_str):
    """
    Recebe uma string e verifica se é uma data válida.
    Parâmetros
    ----------
    data_str : str
        Célula da coluna de datas do início dos sintomas.

    Retorno
    -------
    Bool
        True quando o valor é inválido e False caso contrário.
    """
    try:
        datetime.strptime(data_str, '%d/%m/%Y')
        return False
    except (TypeError, ValueError):
        return True
<<<<<<< HEAD
    
def rem_inv_dtis(df):  
=======


def rem_inv_dtis(df):  # TODO: CRIAR CSV COM df DE ASSINT/DECIDIR OQ FAZER
>>>>>>> b4eb8beef0370659e8692347b97dc1037cccd503
    """
    Retira linhas com valores inválidos de DT_IS.
    Guarda casos assintomáticos em um novo dataframe.

    Parâmetros
    ----------
    df : pd.DataFrame

    Retorno
    -------
    pd.DataFrame
        Dataframe de assintomáticos.

    Exemplos
    --------
    >>> df3 = pd.df(np.array([[1, pd.NA, 3], [4, '10/05/2002', 6], [4, 'Assintomático', 6], [7, '00/05/2002', 9], [1, 'Assintomático', 3]]),
    ...                    columns=['a', 'DT_IS', 'c'])
    >>> rem_inv_dtis(df3)
    >>> df3
       a          DT_IS  c
    1  4     10/05/2002  6
    2  4  Assintomático  6
    4  1  Assintomático  3

    """
    df_assint = df.query('DT_IS == "Assintomático"')
    inval_dtis = df[df['DT_IS'].apply(ftr_dt_is)]
    df_errassint = inval_dtis.query('DT_IS != "Assintomático"')  # df com apenas linhas erradas de dt_is
    df.drop(df_errassint.index, inplace=True)
    return df_assint


def is_integer(value):
    """
    Testa se o valor pode ser convertido em inteiro.

    Parâmetros
    ----------
    value : str

    Retorno
    -------
    Bool
        True se é inteiro e False caso contrário.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def ftr_idades(df):
    """
    Recebe o dataframe e trata a coluna de idades.
    Valores não inteiros são tornados válidos e linhas com idades 0
    e maiores que 130 são retiradas do dataframe principal e separados
    em um dataframe de erro.

    Parâmetros
    ----------
    df : pd.DataFrame

    Retorno
    -------
    pd.DataFrame
        Dataframe com as linhas contendo idades descartadas.

    Exemplos
    -------
    >>> dic2 = {'c1': [1,2,3], 'IDADE': [4,'0,6',6], 'c3': [7,8,9]}
    >>> df3=pd.DataFrame(dic2)
    >>> df3
       c1 IDADE  c3
    0   1     4   7
    1   2   0,6   8
    2   3     6   9
    >>> ftr_idades(df3)
       c1 IDADE  c3
    1   2     0   8
    """
    df_erridade = df.loc[df['IDADE'].apply(lambda x: not is_integer(x))]
    df_erridade.loc[:, 'IDADE'] = df_erridade['IDADE'].astype(str)
    df_erridade.loc[:, 'IDADE'] = df_erridade['IDADE'].str.split(',').str[0]

    df.loc[df_erridade.index] = df_erridade.values

    df_erridd = df[(df['IDADE'].astype(int) < 1) | (df['IDADE'].astype(int) > 130)]

    df.drop(df_erridd.index, inplace=True)

    return df_erridd


def rem_inv_obitos(df):
    """
    Remove linhas com valores inválidos na coluna de óbitos.

    Parâmetros
    ----------
    df : pd.DataFrame

    Exemplos
    --------
    >>> dic2 = {'c1': [1,2,3], 'OBITO': ['SIM',5,'NÃO'], 'c3': [7,8,9]}
    >>> df2 = pd.DataFrame(dic2)
    >>> rem_inv_obitos(df2)
    >>> df2
       c1 OBITO  c3
    1   2     5   8
    """
    inv_obitos = df.query('OBITO != "NÃO" & OBITO != "SIM"')  # df com apenas linhas erradas de óbitos
    df.drop(inv_obitos.index, inplace=True)

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
    nan_cleaner(df)
    rem_inv_dtis(df)
    ftr_idades(df)
    rem_inv_obitos(df)
    df_limpo = rem_dupli(df)
    return df_limpo


#######Funções de Filtragem


def adicionar_coluna(df, nome_coluna, arr_valores):
    """
    Adiciona uma nova coluna ao dataframe cujos valores são fornecidos pela array.

    Parâmetros
    ----------
    df : pd.DataFrame
        O dataframe ao qual a nova coluna será adicionada.
    nome_coluna : str
        O nome da nova coluna.
    arr_valores : dict, np.array, pd.Series
        Os valores a serem inseridos na nova coluna. Pode ser um dicionário, um array NumPy ou uma série Pandas.

    Retorno
    -------
    pd.DataFrame
        O dataframe original com a nova coluna adicionada, ou None em caso de exceção.

    Exemplos
    --------
    >>> dic1 = {'a': [1, 2, 3],
    ...         'b': [4, 5, 6]}
    >>> df = pd.DataFrame(dic1)

    >>> val1 = [10, 20, 30]
    >>> df = adicionar_coluna(df, 'c', val1)
    >>> df
       a  b   c
    0  1  4  10
    1  2  5  20
    2  3  6  30
    """
    try:
        if isinstance(arr_valores, dict):
            arr_valores = pd.Series(arr_valores)
        elif isinstance(arr_valores, np.ndarray):
            valores = pd.Series(valores.tolist())

        if len(arr_valores) != len(df):
            raise ValueError("O número de elementos da array deve ser igual ao número de linhas no df.")

        df[nome_coluna] = arr_valores
        return df
    except Exception as excp:
        print(f"Erro ao adicionar a nova coluna: {excp}")
        return None


def remover_coluna(df, coluna):
    """
    Remove uma coluna específica de um DataFrame.

    Parâmetros
    ----------
    df: pd.DataFrame
        O dataframe original.
    coluna : str
        O nome da coluna a ser removida.

    Retorno
    -------
    pd.DataFrame
        O dataframe original com a coluna removida.

    Exemplo
    -------
    >>> dic3 = {'a': [1, 2, 3],
    ...         'b': [4, 5, 6],
    ...         'c': [7, 8, 9]}
    >>> df3 = pd.DataFrame(dic3)

    >>> df3 = remover_coluna(df3, 'b')
    >>> df3
       a  c
    0  1  7
    1  2  8
    2  3  9
    """
    try:
        if coluna in df.columns:
            df = df.drop(coluna, axis=1)
            return df
        else:
            raise KeyError(f"A coluna '{coluna}' não existe no dataframe.")
    except Exception as expt:
        print(f"Erro ao remover a coluna: {expt}")
        return None


def operacao_colunas(df, colunas, nova_coluna, operacao):
    """
    Realiza uma operação entre colunas do dataframe e cria uma nova coluna com o resultado.

    Parâmetros
    ----------
    df : pd.DataFrame
        Dataframe que contém as colunas originais.
    colunas : dict, np.array, pd.Series, list
        Lista com as colunas a serem usadas na operação. Pode ser um dicionário, u
        ma array NumPy, uma série Pandas ou uma lista de nomes de colunas.
    nova_coluna : str
        Nome da coluna que será criada para armazenar o resultado da operação.
    operacao : function ou str
        A operação a ser realizada. Pode ser uma função ou uma string ('+', '-', '*', '/', 'media', 'dvp', 'mediana', 'min', 'max').
    custom_func : function
        Uma função customizada que pode ser usada como operação.

    Retorno
    -------
    pd.DataFrame
        O dataframe original com a nova coluna .

    Exemplo
    -------
    >>> dic2 = {'c1': [1, 2, 3],
    ...         'c2': [4, 5, 6],
    ...         'c3': [7, 8, 9]}
    >>> df2 = pd.DataFrame(dic2)

    >>> df2 = operacao_colunas(df2, ['c1', 'c2', 'c3'], 'Soma', '+')

    >>> df2 = operacao_colunas(df2, ['c1', 'c2', 'c3'], 'Média', 'media')

    >>> custom_function = lambda x: x['c1'] * 2 + x['c2'] - x['c3']
    >>> df2 = operacao_colunas(df2, ['c1', 'c2', 'c3'], 'Resultado', custom_function)
    >>> df2
        c1  c2  c3  Soma  Média  Resultado
    0   1   4   7    12    4.0         -1
    1   2   5   8    15    5.0          1
    2   3   6   9    18    6.0          3
    """
    try:
        if isinstance(colunas, dict):
            colunas = pd.Series(colunas)
        elif isinstance(colunas, np.ndarray):
            colunas = pd.Series(colunas.tolist())
        elif isinstance(colunas, list):
            colunas = df[colunas]

        if isinstance(operacao, str):
            if operacao == '+':
                df[nova_coluna] = colunas.sum(axis=1)
            elif operacao == '-':
                df[nova_coluna] = colunas.diff(axis=1).fillna(colunas.iloc[:, 0])
            elif operacao == '*':
                df[nova_coluna] = colunas.prod(axis=1)
            elif operacao == 'media':
                df[nova_coluna] = colunas.mean(axis=1)
            elif operacao == 'dvp':
                df[nova_coluna] = colunas.std(axis=1)
            elif operacao == 'mediana':
                df[nova_coluna] = colunas.median(axis=1)
            elif operacao == 'max':
                df[nova_coluna] = colunas.max(axis=1)
            elif operacao == 'min':
                df[nova_coluna] = colunas.min(axis=1)
            else:
                raise ValueError(
                    "Operação inválida. Escolha entre '+', '-', '*', 'media', 'dvp', 'mediana, 'max' ou 'min")
        elif callable(operacao):
            df[nova_coluna] = operacao(colunas, colunas.columns)
        else:
            raise ValueError("O argumento 'operacao' deve ser uma função ou uma string.")

        return df
    except (KeyError, ValueError) as excp:
        print(f"Erro ao realizar a operação: {excp}")
        return None


def filtra_dados(df, colunas=None, linhas=None, nome_csv=None):
    """
    Filtra colunas ou linhas de um dataframe, gerando um novo dataframe com
    os dados selecionados e opcionalmente os salva em um arquivo CSV.

    Parâmetros
    ----------
    df : pd.DataFrame
        Dataframe original.
    colunas : list, dict, np.array, pd.Series
        Colunas a serem selecionadas. Pode ser uma lista de nomes de colunas, um dicionário, np.array ou uma série Pandas.
        Se não especificadas, todas as colunas são selecionadas.
    linhas : slice, list, dict, np.array, pd.Series
        Linhas a serem selecionadas. Pode ser uma slice, uma lista de índices, um dicionário, np.array ou uma série Pandas.
        Se não especificadas, todas as linhas são selecionadas.
    nome_csv : str
        Nome do arquivo CSV para salvar os dados. Se fornecido, os dados serão salvos em um arquivo CSV com esse nome.

    Retorno
    -------
    pd.DataFrame
        Dataframe gerado com os dados selecionados.

    Exemplo
    -------
    >>> dic5 = {'a': [1, 2, 3],
    ...         'b': [4, 5, 6],
    ...         'c': [7, 8, 9]}
    >>> df5 = pd.DataFrame(dic5)

    >>> df_fil = filtra_dados(df, colunas=['a', 'b'])
    >>> df_fil
       a  b
    0  1  4
    1  2  5
    2  3  6

    >>> df_fil = filtra_dados(df, linhas=slice(1, 3))
    >>> df_fil
       a  b  c
    1  2  5  8
    2  3  6  9
    """
    try:
        df_fil = df.copy()

        if colunas is not None:
            if isinstance(colunas, (list, dict, pd.Series, np.ndarray)):
                df_fil = df_fil[colunas]
            else:
                raise ValueError("O argumento 'colunas' deve ser uma lista, dicionário, série ou array NumPy.")

        if linhas is not None:
            if isinstance(linhas, (slice, list, dict, pd.Series, np.ndarray)):
                df_fil = df_fil[linhas]
            else:
                raise ValueError("O argumento 'linhas' deve ser uma slice, lista, dicionário, série ou array NumPy.")

        if nome_csv:
            df_fil.to_csv(nome_csv, index=False)

        return df_fil
    except Exception as expt:
        print(f"Erro ao selecionar os dados: {expt}")
        return None