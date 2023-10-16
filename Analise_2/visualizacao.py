import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors

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
    anos = df['ANO_IS']
    infectados = df['INFECTADOS']
    obitos = df['OBITO']

    # Plotagem das séries de valores em um gráfico de linhas
    plt.plot(anos,infectados,label='Infectados', color='#471164')
    plt.plot(anos,obitos,label='Óbitos', color='#fb9d07')

    # Configuração da plotagem (legendas, títulos, etc)
    definir_rotulos('Ocorrências de Infectados e Óbitos por Ano',
                    'Ano','Ocorrências')
    plt.legend()
    plt.grid(True)
    plt.show()

    return None

def plotar_mortes_por_mes(df: pd.DataFrame) -> None:
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
    meses = df['MES_IS']
    infectados = df['INFECTADOS']
    obitos = df['OBITO']

    # Plotagem das séries de valores em um gráfico de linha #2fb47c
    plt.plot(meses, infectados, label='Infectados', color='#471164', marker='o')  # Adicionado marcadores para os pontos
    plt.plot(meses, obitos, label='Óbitos', color='#fb9d07', marker='o')  # Adicionado marcadores para os pontos

    # Configuração da plotagem (legendas, títulos, etc)
    plt.title('Total de óbitos e infecções por mês')
    plt.xlabel('Mês')
    plt.ylabel('Ocorrências')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=30)  # Defina a rotação das etiquetas do eixo x (30 graus)
    plt.subplots_adjust(top=0.9, bottom=0.18, left=0.13, right=0.90)  # Ajuste das margens
    plt.show()


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
    anos = df['ANO_IS']
    infectados = df['INFECTADOS']
    letalidade = df['LETALIDADE']

    # Configuração da plotagem (legendas, títulos, etc)



    plt.figure(figsize=[8,5])

    plt.scatter(anos, letalidade, c=infectados, cmap='viridis', s=100, zorder=2)
    plt.plot(anos, letalidade, zorder=1)
    plt.colorbar(label='Infectados')
    plt.title("Relação entre Letalidade e Infecções por Ano")
    plt.ylabel("Letalidade")
    plt.grid(axis='y',linestyle='--')
    plt.show()

    return None
