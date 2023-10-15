import pandas as pd
import numpy as np
import re
from datetime import datetime

df = pd.read_csv('fa_casoshumanos_1994-2021.csv', sep = ';', encoding='ISO-8859-1')
df.set_index('ID', inplace = True)



def nan_cleaner(df):
    """
    Cria um dataframe apenas com as linhas que possuem valores NaN 
    e modifica o dataframe original, retirando-as.

    Parâmetros
    ----------
    df : DataFrame
    Retorno
    -------
    DataFrame 
        Dataframe destacado com linhas NaN.
    Exemplos
    --------
    >>> df1 = pd.DataFrame(np.array([[1, 2, 3], [4, pd.NA, 6], [7, 8, 9]]),
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

def rem_dupli(df):
    """
    Remove linhas duplicadas.

    Parâmetros
    ----------
    df : DataFrame
    Retorno
    -------
    DataFrame 
        Dataframe atualizado.
    Exemplos
    --------
    >>> df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [4, 5, 6], [7, 8, 9], [1, 2, 3]]),
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
    
def rem_inv_dtis(df):  #TODO: CRIAR CSV COM DATAFRAME DE ASSINT/DECIDIR OQ FAZER
    """
    Retira linhas com valores inválidos de DT_IS.

    Parâmetros
    ----------
    df : DataFrame

    Exemplos
    --------
    >>> df3 = pd.DataFrame(np.array([[1, pd.NA, 3], [4, '10/05/2002', 6], [4, 'Assintomático', 6], [7, '00/05/2002', 9], [1, 'Assintomático', 3]]),
    ...                    columns=['a', 'DT_IS', 'c'])
    >>> rem_inv_dtis(df3)
    >>> df3
       a          DT_IS  c
    1  4     10/05/2002  6
    2  4  Assintomático  6
    4  1  Assintomático  3

    """
    inval_dtis = df[df['DT_IS'].apply(ftr_dt_is)]
    df_errassint = inval_dtis.query('DT_IS != "Assintomático"')  #Dataframe com apenas linhas erradas de dt_is
    df.drop(df_errassint.index, inplace = True)
    

#df_assint = df.query('DT_IS == "Assintomático"')    

def is_integer(value):
    """
    Testa se o valor pode ser convertido em inteiro.

    Parâmetros
    ----------
    value : object

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




