import unittest
import pandas as pd
import tratamento_dados as td

class TestFuncoesDoSeuModulo(unittest.TestCase):
    def test_organizar_df_datas(self):
        dados = {'ANO_IS': [2019, 2020, 2021], 'MES_IS': [1.0, 1.0, 4.0], 'OBITO': ['SIM', 'NÃO', 'IGN']}
        df = pd.DataFrame(dados)
        saida = td.organizar_df_datas(df)
        self.assertIsInstance(saida, pd.DataFrame)

    def test_organizar_df_ano(self):
        dados = {'ANO_IS': [2019, 2020, 2021], 'MES_IS': [1.0, 1.0, 4.0], 'OBITO': [1, 1, 0], 'INFECTADOS': [1, 1, 1]}
        df = pd.DataFrame(dados)
        saida = td.organizar_df_ano(df)
        self.assertIsInstance(saida, pd.DataFrame)

    def test_organizar_df_mes(self):
        dados = {'ANO_IS': [2019, 2020, 2021], 'MES_IS': [1.0, 1.0, 4.0], 'OBITO': [1, 1, 0], 'INFECTADOS': [1, 1, 1]}
        df = pd.DataFrame(dados)
        saida = td.organizar_df_mes(df)
        self.assertIsInstance(saida, pd.DataFrame)

    def test_organizar_df_letalidade(self):
        dados = {'ANO_IS': [2019, 2020, 2021], 'OBITO': [10, 3, 30], 'INFECTADOS': [20, 15, 50]}
        df = pd.DataFrame(dados)
        saida = td.organizar_df_letalidade(df)
        self.assertIsInstance(saida, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()

