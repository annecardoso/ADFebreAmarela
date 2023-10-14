import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def definir_rotulos(titulo, eixo_x, eixo_y) :
    plt.title(titulo)
    plt.xlabel(eixo_x)
    plt.ylabel(eixo_y)

    return None


def plot_barras(oritentaco, rotulos, valores):
    """
    Essa função gera uma plotagem de um mapa com uma série de pontos, mostrando a distribuição de
    determinada ocorrência em uma região geográfica.

    Parameters
    ----------
    oritentaco : str
        Indicação da orientação do gŕafico. 'v' para vertical ou 'h' para horizontal.

    Returns
    -------
    void
        A função não retorna nada.

    Raises
    ------
    ValueError
        Uma exceção levantada no caso de um valor ser diferente do esperado.
    """
    if str(oritentaco) not in ('h','v') :
        raise ValueError("Erro! O parâmetro fornecido para 'orientacao' deve estar no seguinte conjunto {'h','v'}")


    # Plota de acordo com a orientação escolhida
    if oritentaco == 'v':
        return plt.bar(rotulos,valores)
    else :
        return plt.barh(rotulos,valores)

    return None


def plot_mapa_uf(gdf_obitos_uf):
    """
    Gera um mapa de calor de óbitos por unidade federativa.

    Parameters
    ----------
    gdf_obitos_uf : GeoDataFrame
        GeoDataFrame contendo dados de óbitos por unidade federativa.
    """

    if gdf_obitos_uf is None:
        # Verifica se o GeoDataFrame foi gerado corretamente
        print("O GeoDataFrame não foi gerado corretamente. Não é possível gerar o mapa.")
        return None

    try:
        # Define um novo mapa de cores indo
        cores_extemos = [(1,0.85,0.85),(0.7,0.1,0.1)] # Lista de cores RGB
        gradiente_cores = (mcolors.LinearSegmentedColormap.
                           from_list("gradiente_vermelho",cores_extemos ,256))

        # Plotagem de um mapa de calor com base nos dados de óbitos
        plotagem_mapa = gdf_obitos_uf.plot(column='OBITO', legend=True,
                                     cmap=gradiente_cores)  # Um gráfico geoespacial é criado usando a coluna ’OBITO’ do DataFrame
        return plotagem_mapa

    except Exception as e:
        # Trata exceção se ocorrer um erro inesperado durante a geração do mapa
        print(f"Erro durante a geração do mapa: {e}")
        return None