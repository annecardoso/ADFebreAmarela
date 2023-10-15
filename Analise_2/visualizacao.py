import matplotlib.pyplot as plt
import pandas as pd

def definir_rotulos(titulo, eixo_x, eixo_y):
    """
    Define os rótulos do gráfico.

    Parâmetros
    ----------
    titulo : str
        Título do gráfico.

    eixo_x : str
        Rótulo do eixo x.

    eixo_y : str
        Rótulo do eixo y.

    Retorno
    -------
    None
    """
    plt.title(titulo)
    plt.xlabel(eixo_x)
    plt.ylabel(eixo_y)
    return None

def plotar_ocorrencias_ano(df:pd.DataFrame) -> None:
    """
    Plota ocorrências de infectados e óbitos por ano.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame contendo informações de infectados e óbitos por ano.

    Retorno
    -------
    None
    """
    # Criação de arrays com as séries de valores
    anos = df.iloc[:,0].values
    infectados = df.iloc[:,1].values
    obitos = df.iloc[:,2].values

    # Plotagem das séries de valores em um gráfico de linhas
    plt.plot(anos,infectados,label='Infectados')
    plt.plot(anos,obitos,label='Óbitos')

    # Configuração da plotagem (legendas, títulos, etc)
    definir_rotulos('Ocorrências de Infectados e Óbitos por Ano',
                    'Ano','Ocorrências')
    plt.legend()
    plt.grid(True)
    plt.show()

    return None

def plotar_mortes_por_mes(df:pd.DataFrame) -> None:
    """
    Plota o total de óbitos e infecções por mês.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame contendo informações de óbitos e infecções por mês.

    Retorno
    -------
    None
    """
    # Criação de arrays com as séries de valores
    meses = df.iloc[:, 0].values
    infectados = df.iloc[:, 1].values
    obitos = df.iloc[:, 2].values

    # Plotagem das séries de valores em um gráfico de linhas
    plt.plot(meses, infectados, label='Infectados')
    plt.plot(meses, obitos, label='Óbitos')

    # Configuração da plotagem (legendas, títulos, etc)
    definir_rotulos('Total de óbitos e infecções por mês',
                    'Mês', 'Ocorrências')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=30) # Defina a rotação das etiquetas do eixo x (30 graus)
    plt.subplots_adjust(top=0.9, bottom=0.18, left=0.13, right=0.90) # Ajuste das margens
    plt.show()

    return None

def plotar_letalidade(df:pd.DataFrame) -> None:
    """
    Plota a variação da letalidade da doença ao longo dos anos.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame contendo informações de letalidade por ano.

    Retorno
    -------
    None
    """
    # Criação de arrays com as séries de valores
    anos = df.iloc[:, 0].values
    letalidade = df.iloc[:, 1].values

    # Plotagem das séries de valores em um gráfico de linhas
    plt.plot(anos, letalidade)

    # Configuração da plotagem (legendas, títulos, etc)
    definir_rotulos('Variação da letalidade da febre amarela',
                    'Ano', 'Letalidade')
    plt.grid(True)
    plt.show()

    return None
