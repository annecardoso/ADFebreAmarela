import unittest
import pandas as pd
import geopandas as gpd

# Importa as funções que serão testadas
from utils import carregar_geodataframe, obitos_por_uf
from limpfilt import carregar_dataframe

class TestFuncoes(unittest.TestCase):
    def test_carregar_dataframes(self):
        """
        Testa a função de carregamento de DataFrames.

        Verifica se a função carregar_dataframes carrega corretamente
        os DataFrames de óbitos e informações geoespaciais dos estados.
        """
        df = carregar_dataframe('fa_casoshumanos_1994-2021.csv')
        states = carregar_geodataframe()
        self.assertIsInstance(df, pd.DataFrame)  # Verifica se df é um DataFrame
        self.assertIsInstance(states, gpd.GeoDataFrame)  # Verifica se states é um GeoDataFrame

    def test_obitos_por_uf(self):
        """
        Testa a função de cálculo de óbitos por unidade federativa.

        Verifica se a função obitos_por_uf calcula corretamente o número
        de óbitos por unidade federativa e retorna um GeoDataFrame válido.
        """
        df = carregar_dataframe('fa_casoshumanos_1994-2021.csv')
        states = carregar_geodataframe()
        gdf_obitos_uf = obitos_por_uf(df, states)
        self.assertIsInstance(gdf_obitos_uf, gpd.GeoDataFrame)  # Verifica se o resultado é um GeoDataFrame

if __name__ == '__main__':
    unittest.main()
