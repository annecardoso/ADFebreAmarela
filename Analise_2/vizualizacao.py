import matplotlib.pyplot as plt
import pandas as pd

def definir_rotulos(titulo, eixo_x, eixo_y) :
    plt.title(titulo)
    plt.xlabel(eixo_x)
    plt.ylabel(eixo_y)

    return None


def plotar_ocorrencias_ano(df:pd.DataFrame) -> None:

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
    # Criação de arrays com as séries de valores
    meses = df.iloc[:, 0].values
    infectados = df.iloc[:, 1].values
    obitos = df.iloc[:, 2].values

    # Plotagem das séries de valores em um gráfico de linhas
    plt.plot(meses, infectados, label='Infectados')
    plt.plot(meses, obitos, label='Óbitos')

    # Configuração da plotagem (legendas, títulos, etc)
    definir_rotulos('Ocorrências de Infectados e Óbitos por Ano',
                    'Ano', 'Ocorrências')
    plt.legend()
    plt.grid(True)
    plt.show()

    return None


def plotar_letalidade(df:pd.DataFrame) -> None:
    # Criação de arrays com as séries de valores
    anos = df.iloc[:, 0].values
    letalidade = df.iloc[:, 1].values

    # Plotagem das séries de valores em um gráfico de linhas
    plt.plot(anos, letalidade, label='Letalidade')

    # Configuração da plotagem (legendas, títulos, etc)
    definir_rotulos('Ocorrências de Infectados e Óbitos por Ano',
                    'Ano', 'Ocorrências')
    plt.legend()
    plt.grid(True)
    plt.show()

    return None
