import matplotlib.pyplot as plt
import pandas as pd

def plotar_ocorrencias_ano(df: pd.DataFrame) -> None:
    """
    Plota ocorrências de infectados e óbitos por ano.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contendo informações de infectados e óbitos por ano.

    Returns
    -------
    None
    """
    try:
        # Tentar acessar as colunas necessárias no DataFrame
        anos = df['ANO_IS']
        infectados = df['INFECTADOS']
        obitos = df['OBITO']
    except KeyError as e:
        # Se não existir uma das colunas, captura a exceção e fornece uma mensagem de erro
        print(f"Erro: A coluna {e} não está presente no DataFrame.")
        return None

    try:
        # Criação de um gráfico de linha com duas séries de valores
        plt.plot(anos, infectados, label='Infectados', color='#471164')  # Linha dos infectados
        plt.plot(anos, obitos, label='Óbitos', color='#fb9d07')  # Linha dos óbitos

        # Configuração da plotagem (legendas, títulos, etc)
        plt.title('Ocorrências de Infectados e Óbitos por Ano')
        plt.xlabel('Ano')
        plt.ylabel('Ocorrências')
        plt.legend()  # Habilita a legenda
        plt.grid(True)  # Habilita a grade no gráfico
        plt.show()
        return None
    except Exception as e:
        print(f'Erro ao plotar o gráfico: {e}')


def plotar_mortes_por_mes(df: pd.DataFrame) -> None:
    """
    Plota o total de óbitos e infecções por mês.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contendo informações de óbitos e infecções por mês.

    Returns
    -------
    None
    """
    try:
        # Tenta acessar as colunas necessárias no DataFrame
        meses = df['MES_IS']
        infectados = df['INFECTADOS']
        obitos = df['OBITO']
    except KeyError as e:
        # Se não existir uma das colunas, captura a exceção e fornece uma mensagem de erro
        print(f"Erro: A coluna {e} não está presente no DataFrame.")
        return None

    try:
        # Criação de um gráfico de linha com duas séries de valores
        plt.plot(meses, infectados, label='Infectados', color='#471164', marker='o')  # Linha dos infectados
        plt.plot(meses, obitos, label='Óbitos', color='#fb9d07', marker='o')  # Linha dos óbitos

        # Configuração da plotagem (legendas, títulos, etc)
        plt.title('Total de óbitos e infecções por mês')
        plt.xlabel('Mês')
        plt.ylabel('Ocorrências')
        plt.legend()  # Habilita a legenda
        plt.grid(True)  # Ativa a grade no gráfico
        plt.xticks(rotation=30)  # Rotaciona os rótulos do eixo x em 30 graus
        plt.subplots_adjust(top=0.9, bottom=0.18, left=0.13, right=0.90)  # Ajuste das margens
        plt.show()
        return None
    except Exception as e:
        print(f'Erro ao plotar o gráfico: {e}')


def plotar_letalidade(df: pd.DataFrame) -> None:
    """
    Plota a variação da letalidade da doença ao longo dos anos.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contendo a letalidade e óbitos por ano.

    Returns
    -------
    None
    """
    try:
        # Tentar acessar as colunas necessárias no DataFrame
        anos = df['ANO_IS']
        infectados = df['INFECTADOS']
        letalidade = df['LETALIDADE']
    except KeyError as e:
        # Se não existir uma das colunas, captura a exceção e fornece uma mensagem de erro
        print(f"Erro: A coluna {e} não está presente no DataFrame.")
        return None

    try:
        # Dimensões do gráfico
        plt.figure(figsize=[8, 5])
        # Cria gráfico de dispersão com cores
        plt.scatter(anos, letalidade, c=infectados, cmap='viridis', s=80, zorder=2)
        plt.plot(anos, letalidade, zorder=1)  # Cria uma linha de tendência
        plt.colorbar(label='Infectados')  # Cria uma barra de cores (legenda)

        # Configuração da plotagem (legendas, títulos, etc)
        plt.title("Relação entre Letalidade e Infecções por Ano")
        plt.ylabel("Letalidade")
        plt.grid(axis='y', linestyle='--')  # Grade no eixo y com estilo de linha tracejada
        plt.gca().yaxis.set_major_formatter('{:.0%}'.format)  # Formatação da escala no eixo y em porcentagem
        plt.show()
        return None
    except Exception as e:
        print(f'Erro ao plotar o gráfico: {e}')
