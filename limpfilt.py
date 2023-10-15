import pandas as pd
import numpy as np
import re
from datetime import datetime

df = pd.read_csv('fa_casoshumanos_1994-2021.csv', sep = ';', encoding='ISO-8859-1')
df.set_index('ID', inplace = True)



def nan_cleaner(df):
    """
    Cria um df apenas com as linhas que possuem valores NaN 
    e modifica o df original, retirando-as.

    Parâmetros
    ----------
    df : df
    Retorno
    -------
    df 
        df destacado com linhas NaN.
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
    df.dropna(inplace = True)
    return na_df

nan_cleaner(df)

def rem_dupli(df):
    """
    Remove linhas duplicadas.

    Parâmetros
    ----------
    df : df
    Retorno
    -------
    df 
        df atualizado.
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
    df.drop_duplicates(inplace = True)
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
    except (TypeError,ValueError):
        return True
    
def rem_inv_dtis(df):  #TODO: CRIAR CSV COM df DE ASSINT/DECIDIR OQ FAZER
    """
    Retira linhas com valores inválidos de DT_IS.
    Guarda casos assintomáticos em um novo df.

    Parâmetros
    ----------
    df : df

    Retorno
    -------
    df
        df de assintomáticos.

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
    df_errassint = inval_dtis.query('DT_IS != "Assintomático"')  #df com apenas linhas erradas de dt_is
    df.drop(df_errassint.index, inplace = True)
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

def ftr_idades(df):   ############DOCTEST
    """
    Recebe o df e trata a coluna de idades.
    Valores não inteiros são tornados válidos e linhas com idades 0 
    e maiores que 130 são retiradas do df principal e separados
    em um df de erro.


    Parâmetros
    ----------
    df : df

    Retorno
    -------
    df
        df com as linhas contendo idades descartadas.
    """
    df_erridade = df.loc[df['IDADE'].apply(lambda x: not is_integer(x))]
    df_erridade.loc[:,'IDADE'] = df_erridade['IDADE'].astype(str)
    df_erridade.loc[:,'IDADE'] = df_erridade['IDADE'].str.split(',').str[0]

    df.loc[df_erridade.index] = df_erridade.values

    df_erridd = df[(df['IDADE'].astype(int) < 1) | (df['IDADE'].astype(int) > 130)]
    
    df.drop(df_erridd.index, inplace = True)

    return df_erridd


#TODO: COLUNA DE MORTES
#TODO: VERIFICAR COM UNIQUE ESTADOS, SEXO...
#TODO: PARTE DE FILTRAGEM

#TODO VISU E ANALISES


#######Funções de Filtragem


def adicionar_coluna(df, nome_coluna, arr_valores):
    """
    Adiciona uma nova coluna ao df cujos valores são fornecidos pela array.

    Parâmetros
    ----------
    df : pd.df
        O df ao qual a nova coluna será adicionada.
    nome_coluna : str
        O nome da nova coluna.
    arr_valores : dict, np.array, pd.Series
        Os valores a serem inseridos na nova coluna. Pode ser um dicionário, um array NumPy ou uma série Pandas.

    Retorno
    -------
    pd.df
        O df original com a nova coluna adicionada, ou None em caso de exceção.

    Exemplos
    --------
    >>> dic1 = {'a': [1, 2, 3],
    ...         'b': [4, 5, 6]}
    >>> df = pd.df(dic1)
    
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



def operacao_colunas(df, colunas, nova_coluna, operacao, custom_func=None):
    """
    Realiza uma operação entre colunas do df e cria uma nova coluna com o resultado.

    Parâmetros
    ----------
    df : pd.df
        df que contém as colunas originais.
    colunas : dict, np.array, pd.Series, list
        Lista com as colunas a serem usadas na operação. Pode ser um dicionário, u
        ma array NumPy, uma série Pandas ou uma lista de nomes de colunas.
    nova_coluna : str
        Nome da coluna que será criada para armazenar o resultado da operação.
    operacao : function ou str
        A operação a ser realizada. Pode ser uma função ou uma string ('+', '-', '*', '/', 'media', 'dvp', 'mediana', 'min', 'max').
    custom_func : function, optional
        Uma função customizada que pode ser usada como operação.

    Retorno
    -------
    pd.df
        O df original com a nova coluna .

    Exemplo
    -------
    >>> dic2 = {'c1': [1, 2, 3],
    ...         'c2': [4, 5, 6],
    ...         'c3': [7, 8, 9]}
    >>> df2 = pd.df(dic2)
    
    >>> # Realiza a adição das colunas 
    >>> df2 = operacao_colunas(df2, ['c1', 'c2', 'c3'], 'Soma', '+')
    
    >>> # Calcula a média das colunas
    >>> df2 = operacao_colunas(df2, ['c1', 'c2', 'c3'], 'Média', 'media')
    
    >>> # Usa uma função personalizada
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
            elif operacao == '/':
                df[nova_coluna] = colunas.apply(lambda x: x.prod(), axis=1)
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
                raise ValueError("Operação inválida. Escolha entre '+', '-', '*', '/', 'media', 'dvp', 'mediana, 'max' ou 'min")
        elif callable(operacao):
            df[nova_coluna] = operacao(colunas)
        else:
            raise ValueError("O argumento 'operacao' deve ser uma função ou uma string.")
        
        return df
    except (KeyError, ValueError) as excp:
        print(f"Erro ao realizar a operação: {excp}")
        return None
